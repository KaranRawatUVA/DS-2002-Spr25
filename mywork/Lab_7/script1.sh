#!/bin/bash
echo "First argument: $1"
echo "Second argument: $2"
echo "Third argument: ${3:-604800}"



file_name=$1
bucket_name=$2
length=${3:-604800}


aws s3 cp $file_name s3://$bucket_name/


aws s3 presign --expires-in $length s3://$bucket_name/$file_name


