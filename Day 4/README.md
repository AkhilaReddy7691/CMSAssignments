##AWS Lambda Function with S3 Deployment

---

This project demonstrates the creation and deployment of a simple AWS Lambda function that interacts with an S3 bucket.

---

##Project Overview

- Lambda Function: A basic Python function deployed in AWS Lambda.
- S3 Bucket: Stores the Lambda deployment package (.zip) and any related resources.
- Deployment: Done via AWS Console.

---

##Files Included

- `lambda_function.py` – Main Lambda function script
-`s3` - added a file

---


##Steps to Create Lambda Function

1. Create an S3 Bucket
   - Upload your `lambda_function.zip` package.
   - Make sure it's in the correct region.

2. Create a Lambda Function
   - Runtime: Python 3.x
   - Upload from: Amazon S3
   - Provide S3 URL of your zip file

3. Test the Function
   - Create a test event
   - Check logs via CloudWatch

---


##Notes

- Make sure your IAM role has appropriate permissions (`AWSLambdaBasicExecutionRole`, `AmazonS3ReadOnlyAccess`)
- Keep S3 bucket and Lambda in the same region

---


![lambda1](https://github.com/user-attachments/assets/c7f9ebd6-0f4b-465e-ad8f-b15b5dc2c514)

![lambda2](https://github.com/user-attachments/assets/7089f304-443d-42da-9162-1fd60210c2e0)

![lambda3](https://github.com/user-attachments/assets/21fe8433-7e4d-47dc-ad13-c08b6abf0cbe)

![lambda4](https://github.com/user-attachments/assets/d3f27920-0421-4682-9c57-ab75bcd716d6)

![lambda5](https://github.com/user-attachments/assets/11beab80-a3d7-4658-a1e7-d2daa6ea32c2)

![lambda6](https://github.com/user-attachments/assets/3a7e02e4-8fec-4e63-aced-9550b099ee61)

![bucket1](https://github.com/user-attachments/assets/6e872a5e-cf7e-433a-ab69-dc982fed1b88)

![bucket2](https://github.com/user-attachments/assets/07acf7d2-73ab-4169-a2e6-8967945b819a)



