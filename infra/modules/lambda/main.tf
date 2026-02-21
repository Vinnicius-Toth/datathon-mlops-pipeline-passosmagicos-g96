resource "aws_lambda_function" "this" {
  function_name = var.lambda_name
  runtime       = "python3.10"
  handler       = "handler.lambda_handler"
  role          = var.lambda_role_arn
  filename      = "lambda/etl.zip"
  timeout       = 300

  tags = var.tags
}