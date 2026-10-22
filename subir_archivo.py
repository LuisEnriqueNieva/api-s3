import base64
import boto3

def lambda_handler(event, context):
    nombre_bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    nombre_archivo = event['body']['nombre_archivo']
    contenido = base64.b64decode(event['body']['contenido'])

    s3 = boto3.client('s3')
    key = directorio.strip('/') + '/' + nombre_archivo
    s3.put_object(Bucket=nombre_bucket, Key=key, Body=contenido)

    return {
        'statusCode': 200,
        'mensaje': 'Archivo subido',
        'bucket': nombre_bucket,
        'key': key
    }
