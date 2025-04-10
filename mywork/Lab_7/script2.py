#!/usr/bin/env python3

import boto3
import requests
import sys
import os
from urllib.parse import urlparse

s3 = boto3.client('s3', region_name='us-east-1')

# Getting Args
file_url = sys.argv[1]
bucket_name = sys.argv[2]
length = 604800
if len(sys.argv) > 3:
    length = int(sys.argv[3])

# Get File

parsed_url = urlparse(file_url)
file_name = os.path.basename(parsed_url.path) 

response = requests.get(file_url, stream=True)  
response.raise_for_status()  

with open(file_name, 'wb') as file:
    for chunk in response.iter_content(1024):  
        file.write(chunk)

#print(f"Image downloaded and saved as {file_name}")

file_path = os.path.abspath(file_name)
#print(f"File path: {file_path}")


# Upload it

s3.upload_file(file_name, bucket_name, file_name)



# S3 Presigned Link

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': file_name},
    ExpiresIn=length,
    )

print(response)

#os.remove(file_name)
