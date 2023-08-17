import os
import boto3
from dotenv import load_dotenv

load_dotenv()

##aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('REGION_NAME')
kms_key_arn = os.getenv('KMS_KEY_ARN')
end_bucket_number = int(os.getenv('END_BUCKET_NUMBER'))

#s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
s3_client = boto3.client('s3', region_name=region_name)

for bucket_number in range(1, end_bucket_number + 1):
    bucket_name = f'lido-bucket-{bucket_number}'
    s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
    s3_client.put_bucket_encryption(
        Bucket=bucket_name,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'aws:kms',
                        'KMSMasterKeyID': kms_key_arn
                    }
                }
            ]
        }
    )
    print(f'{bucket_name} creation completed')

print('Completed creating buckets')