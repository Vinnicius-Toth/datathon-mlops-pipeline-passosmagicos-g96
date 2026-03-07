data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

resource "aws_instance" "this" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type

  key_name = "infra-api-key"

  subnet_id                   = var.subnet_id
  vpc_security_group_ids      = [var.security_group_id]
  associate_public_ip_address = true

  iam_instance_profile = var.iam_instance_profile

  user_data = <<-EOF
              #!/bin/bash
              yum update -y

              amazon-linux-extras install docker -y
              systemctl enable docker
              systemctl start docker

              usermod -aG docker ec2-user
              EOF

  tags = merge(
    var.tags,
    {
      Name = var.instance_name
    }
  )
}