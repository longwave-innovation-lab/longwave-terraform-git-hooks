# This file has locals NOT as the first block - should fail
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

locals {
  environment = "production"
  project_name = "example"
  common_tags = {
    Environment = local.environment
    Project     = local.project_name
  }
}

resource "aws_s3_bucket" "example" {
  bucket = "${local.project_name}-${local.environment}"
  tags   = local.common_tags
}

output "bucket_name" {
  value = aws_s3_bucket.example.bucket
}
