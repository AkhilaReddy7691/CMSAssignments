##AWS Lambda Function with S3 Deployment

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


