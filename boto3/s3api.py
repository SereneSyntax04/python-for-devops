                                    # TASK 2: Get Bucket ACL (Access Control List)

import boto3

# Initialize S3 client
# ⚠️ IMPORTANT: If you are working with multiple scripts (e.g., s3.py and TASK2s3.py),
# you must reinitialize the client in each file separately.
# Otherwise, 'client' will not be defined, and your script will fail.
client = boto3.client("s3")

# Fetch the ACL (Access Control List) of the specified S3 bucket.
# This returns information about the bucket owner and the permissions
# granted to different AWS accounts/users/groups.
response = client.get_bucket_acl(
    Bucket='python-for-devops-project1-2025'
)

# Print the raw ACL response (will include Owner + Grants)
print(response)
