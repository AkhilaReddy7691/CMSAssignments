import boto3, io
from PIL import Image

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    ddb = boto3.resource('dynamodb').Table('ImageMetadata')

    b = event['Records'][0]['s3']['bucket']['name']
    k = event['Records'][0]['s3']['object']['key']
    img = Image.open(io.BytesIO(s3.get_object(Bucket=b, Key=k)['Body'].read()))

    ddb.put_item(Item={'ImageName': k, 'Format': img.format, 'Size': str(img.size), 'Mode': img.mode})
    return {'statusCode': 200, 'body': f'Metadata for {k} stored'}
