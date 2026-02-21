variable "lambda_name" {}
variable "lambda_role_arn" {}
variable "lambda_code_bucket" {}
variable "lambda_code_key" {}
variable "tags" {
  type = map(string)
}