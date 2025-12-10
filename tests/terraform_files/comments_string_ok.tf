data "aws_iam_policy_document" "test_wildcard" {
  statement {
    effect = "Allow"
    actions = [
      "s3:GetObject",
      "s3:ListBucket",
      "s3:GetObjectVersion",
      "s3:GetObjectTagging"
    ]
    resources = [
      data.aws_s3_bucket.my_bucket.arn,
      "${data.aws_s3_bucket.my_bucket.arn}/*"
    ]
  }
}
