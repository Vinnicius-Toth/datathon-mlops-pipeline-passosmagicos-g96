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