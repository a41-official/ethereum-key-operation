import os
import tarfile
import boto3
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load values from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('S3_REGION_NAME')
bucket_name = os.getenv('S3_BUCKET_NAME')
file_key = os.getenv('S3_FILE_KEY')

# AWS client creation
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Download and extract the archive for each bucket
archive_name = file_key  # Archive file name
object_key = f'{archive_name}'

# Download the archive file
s3_client.download_file(bucket_name, object_key, archive_name)

# Extract the archive
with tarfile.open(archive_name, 'r:gz') as tar:
    tar.extractall()

print(f'Archive file {archive_name} downloaded from {bucket_name} and extracted.')

# Delete the downloaded archive file
os.remove(archive_name)

print('All files have been downloaded and extracted.')