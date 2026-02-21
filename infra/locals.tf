locals {
  environment = "prod"

  name_prefix = "${var.project_name}-${local.environment}"

  common_tags = {
    Project     = var.project_name
    Environment = local.environment
    ManagedBy   = "terraform"
  }

  s3_raw_name    = "${local.name_prefix}-raw"
  s3_gold_name   = "${local.name_prefix}-gold"
  s3_model_name  = "${local.name_prefix}-models"

  ecr_repo_name  = "${local.name_prefix}-api"

  vpc_name       = "${local.name_prefix}-vpc"
  subnet_name    = "${local.name_prefix}-public-subnet"
  sg_name        = "${local.name_prefix}-sg"

  lambda_name    = "${local.name_prefix}-etl"
  ec2_name       = "${local.name_prefix}-api"
}