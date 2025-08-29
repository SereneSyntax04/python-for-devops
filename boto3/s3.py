import boto3

# Create an S3 client
# By default boto3 will use your AWS credentials from `~/.aws/credentials` 
# or environment variables (set by `aws configure`).
client = boto3.client('s3')

# Define the AWS region where you want to create the bucket
# NOTE: If you use "us-east-1", you must NOT include CreateBucketConfiguration
region = "ap-south-1"

# Create the bucket
# Bucket naming rules:
#   - must be lowercase
#   - only letters, numbers, dots, and hyphens
#   - must be globally unique across all AWS accounts
response = client.create_bucket(
    Bucket='python-for-devops-project1-2025',   # ✅ valid bucket name
    CreateBucketConfiguration={
        'LocationConstraint': region,   # Required for all regions except "us-east-1"
    },
)

# Print the response from AWS
print("Bucket created:", response)

