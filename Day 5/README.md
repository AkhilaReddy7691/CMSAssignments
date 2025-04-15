##Terraform AWS EC2 Instance Deployment

---

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

---


![terraform1](https://github.com/user-attachments/assets/f52b1f4f-e8c1-4d42-8256-e82e1a3205e6)

![terraform2](https://github.com/user-attachments/assets/008cc9d3-85e7-4c7a-b262-c387231af524)

![terraform3](https://github.com/user-attachments/assets/757652e9-ae54-49e5-9862-6ae481e8240f)

![terraform4](https://github.com/user-attachments/assets/1a3fc9fb-6e3b-460e-b868-c37cd9c0fdb2)







