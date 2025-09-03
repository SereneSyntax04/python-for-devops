import boto3

client = boto3.client("s3")

client.upload_file('/workspaces/python-for-devops/boto3/s3tmp.txt', 'python-for-devops-project1-2025', 's3tmp.txt')