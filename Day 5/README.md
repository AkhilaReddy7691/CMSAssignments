##Terraform AWS EC2 Instance Deployment

This project demonstrates how to use Terraform to provision an EC2 instance on AWS using minimal configuration.

---

##Project Structure

terraform-ec2/ ├── main.tf # Contains the AWS provider config and EC2 resource

---


##What It Does

- Initializes Terraform with AWS as the provider.
- Launches a t2.micro EC2 instance in the us-east-1 region using a specific Amazon Machine Image (AMI).
- Tags the instance as `"FirstServer"`.

---


##Prerequisites

- AWS CLI installed and configured with credentials.
- Terraform installed (version >= 1.2.0).
- An AWS account with permissions to create EC2 instances.

---

##Usage

1. Clone or navigate to your Terraform project folder.

2. Initialize Terraform
   ```bash
   terraform init

3. Validate the configuration

terraform validate

4. Create an execution plan

terraform plan

5. Apply the changes

terraform apply

---

##Access your AWS Console

Go to EC2 Dashboard in the us-east-1 region.

You should see an instance running with the name FirstServer.

#EC2 Instance Details

AMI ID: ami-00a929b66ed6e0de6

Instance Type: t2.micro

Region: us-east-1

Tag: Name = "FirstServer"

---

##Cleanup

To delete the created EC2 instance:

terraform destroy



