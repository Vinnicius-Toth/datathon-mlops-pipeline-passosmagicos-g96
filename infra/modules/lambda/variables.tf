variable "lambda_name" {}
variable "lambda_role_arn" {}
variable "lambda_code_bucket" {}
variable "lambda_code_key" {}
variable "tags" {
  type = map(string)
}
variable "layers" {
  description = "Lista de ARNs de layers para a Lambda"
  type        = list(string)
  default     = []
}