module "s3" {
  source          = "./modules/s3"
  raw_bucket      = local.s3_raw_name
  gold_bucket     = local.s3_gold_name
  model_bucket    = local.s3_model_name
  tags            = local.common_tags
}

# module "vpc" {
#   source      = "./modules/vpc"
#   vpc_name    = local.vpc_name
#   subnet_name = local.subnet_name
#   tags        = local.common_tags
# }

# module "security" {
#   source   = "./modules/security"
#   vpc_id   = module.vpc.vpc_id
#   sg_name  = local.sg_name
#   tags     = local.common_tags
# }

# module "iam" {
#   source = "./modules/iam"
# }

# module "lambda" {
#   source            = "./modules/lambda"
#   lambda_name       = local.lambda_name
#   lambda_role_arn   = module.iam.lambda_role_arn
#   tags              = local.common_tags
# }

# module "ecr" {
#   source    = "./modules/ecr"
#   repo_name = local.ecr_repo_name
#   tags      = local.common_tags
# }

# module "ec2" {
#   source            = "./modules/ec2"
#   instance_name     = local.ec2_name
#   ami_id            = var.ami_id
#   subnet_id         = module.vpc.public_subnet_id
#   security_group_id = module.security.security_group_id
#   tags              = local.common_tags
# }