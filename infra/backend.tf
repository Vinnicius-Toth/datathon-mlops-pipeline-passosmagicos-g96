terraform {
  backend "s3" {
    bucket  = "mlops-pipeline-passosmagicos-artifacts"
    key     = "terraform-state/terraform.tfstate"
    region  = "us-east-2"
    encrypt = true
  }
}