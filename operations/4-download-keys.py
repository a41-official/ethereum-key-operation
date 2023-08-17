import os
import tarfile
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load values from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('REGION_NAME')

# List of S3 bucket names
bucket_names = ['lido-bucket-1', 'lido-bucket-2', 'lido-bucket-3']

# AWS client creation
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Download and extract the archive for each bucket
for index, bucket_name in enumerate(bucket_names, start=1):
    folder_name = f'bucket-{index}'  # Extract the number from the bucket name
    archive_name = f'validator_keys.tar.gz'  # Archive file name
    object_key = f'{archive_name}'
    
    # Download the archive file
    s3_client.download_file(bucket_name, object_key, archive_name)
    
    # Extract the archive
    with tarfile.open(archive_name, 'r:gz') as tar:
        tar.extractall(folder_name)
    
    print(f'Archive file {archive_name} downloaded from {bucket_name} and extracted to {folder_name}.')

    # Delete the downloaded archive file
    os.remove(archive_name)

print('All files have been downloaded and extracted.')