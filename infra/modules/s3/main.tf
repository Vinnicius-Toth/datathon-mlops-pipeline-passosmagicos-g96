resource "aws_s3_bucket" "raw" {
  bucket = var.raw_bucket
  tags   = var.tags
}

resource "aws_s3_bucket" "gold" {
  bucket = var.gold_bucket
  tags   = var.tags
}

resource "aws_s3_bucket" "models" {
  bucket = var.model_bucket
  tags   = var.tags
}

resource "aws_s3_bucket_notification" "raw_trigger" {
  bucket = aws_s3_bucket.raw.id

  lambda_function {
    lambda_function_arn = var.lambda_arn
    events              = ["s3:ObjectCreated:*"]

    filter_prefix = "raw/"
  }

  depends_on = [var.lambda_permission]
}