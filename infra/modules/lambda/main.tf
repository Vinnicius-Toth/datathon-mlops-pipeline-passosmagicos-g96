resource "aws_lambda_function" "this" {
  function_name = var.lambda_name
  role          = var.lambda_role_arn
  runtime       = "python3.10"
  handler       = "handler.lambda_handler"

  s3_bucket = var.lambda_code_bucket
  s3_key    = var.lambda_code_key

  timeout = 300

  tags = var.tags
}