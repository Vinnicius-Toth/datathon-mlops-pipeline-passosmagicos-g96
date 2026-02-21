resource "aws_instance" "api" {
  ami                    = var.ami_id
  instance_type          = "t2.micro"
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [var.security_group_id]

  tags = merge(
    var.tags,
    {
      Name = var.instance_name
    }
  )
}