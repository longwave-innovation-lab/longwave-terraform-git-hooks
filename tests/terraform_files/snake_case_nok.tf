# Here there should be a block where all the locals are defined
locals {
  my-local = "example9"
}

resource "aws_iam_role" "my-role" {
  name = "example"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

output "my-output" {
  value = aws_iam_role.my-role.arn
}

variable "my-variable" {
  default     = "Something"
  type        = string
  description = "This is a description of the variable"
}

data "aws_iam_role" "my-data_role" {
  name = "example-role"
}

module "my-module" {
  source = "git@github.com:example/example.git"
  name   = "example-module"
}
