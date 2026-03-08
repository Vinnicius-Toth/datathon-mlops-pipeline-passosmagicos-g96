module "s3" {
  source       = "./modules/s3"
  raw_bucket   = local.s3_raw_name
  gold_bucket  = local.s3_gold_name
  model_bucket = local.s3_model_name
  tags         = local.common_tags
}

module "vpc" {
  source      = "./modules/vpc"
  vpc_name    = local.vpc_name
  subnet_name = local.subnet_name
  tags        = local.common_tags
}

module "security" {
  source   = "./modules/security"
  vpc_id   = module.vpc.vpc_id
  sg_name  = local.sg_name
  tags     = local.common_tags
}

module "iam" {
  source = "./modules/iam"
}

module "lambda" {
  source              = "./modules/lambda"
  lambda_name         = local.lambda_name
  lambda_role_arn     = module.iam.lambda_role_arn
  lambda_code_bucket  = "mlops-pipeline-passosmagicos-artifacts"
  lambda_code_key     = "lambda/handler.zip"
  tags                = local.common_tags
}

resource "aws_lambda_permission" "allow_s3" {
  statement_id  = "AllowExecutionFromS3"
  action        = "lambda:InvokeFunction"
  function_name = module.lambda.lambda_name
  principal     = "s3.amazonaws.com"
  source_arn    = module.aws_s3_bucket.raw_bucket_arn
}

resource "aws_s3_bucket_notification" "raw_trigger" {
  bucket = module.aws_s3_bucket.raw_bucket_id

  lambda_function {
    lambda_function_arn = module.lambda.lambda_arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "raw/"
  }

  depends_on = [
    aws_lambda_permission.allow_s3
  ]
}


module "ecr" {
  source          = "./modules/ecr"
  repository_name = local.ecr_repo_name
  tags            = local.common_tags
}

module "ec2" {
  source            = "./modules/ec2"
  instance_name     = local.ec2_name
  instance_type     = "t3.micro"
  subnet_id         = module.vpc.public_subnet_id
  security_group_id = module.security.security_group_id
  iam_instance_profile = module.iam.ec2_instance_profile_name
  tags              = local.common_tags
}