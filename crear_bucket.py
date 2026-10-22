import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    s3 = boto3.client('s3')
  
    try:
        s3.create_bucket(Bucket=nombre_bucket)
    except ClientError as e:
        return {'statusCode': 400, 'mensaje': e.response['Error']['Code']}
      
    return {
        'statusCode': 200,
        'mensaje': 'Bucket creado',
        'bucket': nombre_bucket
    }
