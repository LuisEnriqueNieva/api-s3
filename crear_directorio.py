import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']

    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=directorio.strip('/') + '/')

    return {
        'statusCode': 200,
        'mensaje': 'Directorio creado',
        'bucket': nombre_bucket,
        'directorio': directorio
    }
