import os
import tarfile
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load values from environment variables
#aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
#aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('REGION_NAME')

# List of S3 bucket names
bucket_names = ['lido-bucket-1', 'lido-bucket-2', 'lido-bucket-3']

# Create AWS client
#s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
s3_client = boto3.client('s3', region_name=region_name)

# Compress and upload validator_keys directory for each bucket
for index, bucket_name in enumerate(bucket_names, start=1):
    folder_name = f'bucket-{index}'  # Extract the number from the bucket name
    archive_name = f'validator_keys.tar.gz'  # Archive file name
    
    # Compress the validator_keys directory
    with tarfile.open(archive_name, 'w:gz') as tar:
        tar.add(os.path.join(folder_name, 'validator_keys'), arcname='validator_keys')
    
    # Upload the compressed file to the S3 bucket
    object_key = f'{archive_name}'
    s3_client.upload_file(archive_name, bucket_name, object_key)
    
    print(f'Archive file {archive_name} uploaded to the {bucket_name} bucket.')

    # Delete the created archive file
    os.remove(archive_name)

print('All file uploads have been completed.')
