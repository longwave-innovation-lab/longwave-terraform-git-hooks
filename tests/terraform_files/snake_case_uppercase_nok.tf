# Here there should be a block where all the locals are defined
locals {
  my_LOCAL  = "example"
}

resource "aws_iam_role" "my_ROLE" {
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

output "my_OUTPUT" {
  value = aws_iam_role.my-role.arn
}

variable "my_VARIABLE" {
  default     = "Something"
  type        = string
  description = "This is a description of the variable"
}

data "aws_iam_role" "my_DATA_ROLE" {
  name = "example-role"
}

module "my_MODULE" {
  source = "git@github.com:example/example.git"
  name   = "example-module"
}
