# This is a valid comment
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"

  # Another valid comment
  tags = {
    Name = "Example"
  }
}

# Multiple lines
# are also fine
variable "example" {
  description = "Example variable"
  type        = string
  default     = "value"
}
