# This file has locals as the first block - should pass

# Commented resource to test if the file is parsed correctly
# resource "aws_instance" "example" {
#   ami           = "resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
#   instance_type = "t3.micro"

#   tags = {
#     Name = "HelloWorld"
#   }
# }

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

variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

output "bucket_name" {
  value = aws_s3_bucket.example.bucket
}
