resource "aws_lambda_function" "this" {
  function_name = var.lambda_name
  role          = var.lambda_role_arn
  runtime       = "python3.10"
  handler       = "handler.lambda_handler"

  s3_bucket = var.lambda_code_bucket
  s3_key    = var.lambda_code_key

  memory_size = 1024
  timeout = 300

  tags = var.tags
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = module.lambda.lambda_name
  principal     = "s3.amazonaws.com"
  source_arn    = module.s3.raw_bucket_arn
}