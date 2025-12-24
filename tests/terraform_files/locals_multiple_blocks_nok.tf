# This file has locals as the first block but also locasls
# not as the first block - It should fail
locals {
  sample_value = "example"
}

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
