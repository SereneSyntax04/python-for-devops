import boto3

client = boto3.client('s3')

client.download_file('python-for-devops-project1-2025', 's3_download_file.txt', '/workspaces/python-for-devops/boto3/s3_download_file.txt')
