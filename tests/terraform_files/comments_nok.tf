// This is an invalid comment style
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"

  /* This is also invalid */
  tags = {
    Name = "Example"
  }
}

/* Multi-line
   block comment
   is not allowed */
variable "example" {
  description = "Example variable"
  type        = string
  default     = "value"
}
