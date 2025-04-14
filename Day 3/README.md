##AWS EKS Cluster Setup 

This guide explains how to create a Kubernetes cluster on Amazon EKS using the terminal inside Visual Studio Code (`VS Code`) and deploy workloads that will reflect in the AWS EKS Console.

---

##Prerequisites

Make sure you have the following installed:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [eksctl](https://eksctl.io/introduction/#installation)
- [Visual Studio Code](https://code.visualstudio.com/)

---

##AWS CLI Configuration

First, configure your AWS credentials:

```bash
aws configure

Provide:

Access Key ID

Secret Access Key

Region (e.g., ap-south-1)

Output format (e.g., json)

---

###Create EKS Cluster (From VS Code Terminal)

Step 1: Open VS Code Terminal

Click Terminal > New Terminal


Step 2: Run the Cluster Creation Command

eksctl create cluster \
  --name my-cluster \
  --region ap-south-1 \
  --nodegroup-name nginx-nodes \
  --node-type t3.medium \
  --nodes 2 \
  --nodes-min 1 \
  --nodes-max 3 \
  --managed

This will take about 10–15 minutes to finish.

---

##View in AWS Console

Go to your AWS Console:

Navigate to EKS > Clusters

Select my-cluster

You will see:

Cluster Overview

Node Groups

Workloads (once deployed)

Networking details

---

##To Delete the Cluster (Optional)

eksctl delete cluster --name my-cluster --region ap-south

---

##Notes

Make sure your AWS CLI and IAM role have the right permissions for EKS.

Use proper naming conventions and choose a region closest to you.
