output "lambda_role_arn" {
  value = aws_iam_role.lambda_role.arn
}

output "ec2_instance_profile_name" {
  description = "Instance profile for EC2"
  value       = aws_iam_instance_profile.ec2_profile.name
}