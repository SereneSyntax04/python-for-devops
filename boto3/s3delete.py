
import boto3

client = boto3.client("s3")

client.delete_bucket(Bucket="python-for-devops-project1-2025")  # cange the name accordingly
print("Bucket deleted")

# creating this separatly so we can delete the bucket once the usage is done.