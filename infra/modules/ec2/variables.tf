variable "instance_name" {}
variable "instance_type" {}
variable "subnet_id" {}
variable "security_group_id" {}
variable "tags" {
  type = map(string)
}
variable "iam_instance_profile" {
  description = "IAM Instance Profile for EC2"
  type        = string
}