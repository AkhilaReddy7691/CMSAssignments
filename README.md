### DevOps Cloud Journey – From Docker to Terraform

Welcome to the end-to-end DevOps project setup! This repository contains a structured series of assignments and projects covering Docker, Kubernetes, AWS services (EKS, Lambda), and Terraform. It’s designed to demonstrate modern infrastructure management and deployment practices.

---

##Day 1: Docker – Containerization Basics

In this section, we build a basic Python web scraper app using Docker.

###Features

- Python script to scrape book data from a website.
- Saves the scraped data in a CSV file.
- Simple HTTP server to serve files.
- Dockerized the entire app.

###Docker Commands

docker build -t webscrapper-images .

docker run -p 8000:8000 webscrapper-images

#Output

Open your browser and go to: http://localhost:8000/scraped_books.csv

---

##Day 2: Kubernetes – Deploying with K8s

We move from containers to orchestration using Kubernetes to manage deployments at scale.

##Features

Pod and Deployment creation using YAML.

Exposed services using NodePort.

Explored basic kubectl operations.


kubectl apply -f quiz-app-deployment.yaml

kubectl apply -f quiz-app-service.yaml

---

##Day 3: AWS EKS – Kubernetes in the Cloud

We deploy our Kubernetes workloads into a managed AWS EKS cluster.

##Features

Created EKS cluster using AWS CLI or console.

Configured kubectl to access EKS.

Deployed workloads via manifests.

Managed autoscaling and IAM roles.

##Tools Used

eksctl

kubectl

IAM Roles for Service Accounts (IRSA)

---

##Day 4: AWS Lambda – Serverless Functions

We explore serverless computing using AWS Lambda for lightweight, event-driven automation.

##Features

Created Python-based Lambda function.

Integrated with API Gateway.

Triggered via HTTP request or S3 event.

#Files

lambda_function.py

---


###Day 5: Terraform – Infrastructure as Code

We finish by managing all infrastructure components using Terraform.

##Features

Launched an EC2 instance using main.tf.

Managed AWS provider and region.

Used terraform init, apply, destroy.

##main.tf

provider "aws" {

  region = "us-east-1"
  
}

resource "aws_instance" "app_server" {

  ami           = "ami-00a929b66ed6e0de6"
  
  instance_type = "t2.micro"

  tags = {
  
    Name = "FirstServer" 
    
  }
  
}


##Commands

terraform init

terraform validate

terraform plan

terraform apply

terraform destroy

---

##Summary

Tool	      -          Focus	              -                   Highlights

Docker	     -     Containerization	        -         Simple app in a lightweight image

Kubernetes	 -     Orchestration	          -           Scalable deployments and services

AWS EKS	     -    Managed Kubernetes	      -         Cloud-native orchestration

AWS Lambda	 -    Serverless Functions	    -        Event-driven automation

Terraform	   -     Infrastructure as Code (IaC)  -     Declarative resource provisioning
