variable "raw_bucket" {}
variable "gold_bucket" {}
variable "model_bucket" {}
variable "tags" {
  type = map(string)
}
variable "lambda_arn" {}
variable "lambda_permission" {}