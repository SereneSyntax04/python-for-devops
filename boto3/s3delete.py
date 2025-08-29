
import boto3

client = boto3.client("s3")

client.delete_bucket(Bucket="python-for-devops-project1-2025")
print("Bucket deleted")