# BOTO3:
Boto3 is basically AWS’s official SDK (Software Development Kit) for Python. <br>
It’s the tool you use when you want Python code to talk to AWS services like S3, EC2, DynamoDB, Lambda, IAM, etc. <br>

Think of it like this: instead of logging into the AWS console every time you want to create a bucket, upload a file, or launch an EC2 instance, you just write Python code with boto3 and it does the job for you.

---

## How boto3 is structured

It has two main layers:

1. Client – A low-level way of talking directly to AWS APIs. <br>
Example:
```python
import boto3

s3_client = boto3.client('s3')
s3_client.create_bucket(Bucket='my-bucket-name')
```
This is very “API-style” — you’re calling methods that directly map to AWS service APIs.


2. Resource – A higher-level, more Pythonic abstraction.
Example:
```python
import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('my-bucket-name')
bucket.upload_file('local_file.txt', 'remote_file.txt')
```
This feels more like working with Python objects than raw API calls.



---


## DIFFERENCE
There are multiple tools to work with AWS: CFT, Terraform, AWS CLI, and boto3.
1. CloudFormation (CFT) & Terraform
- Template-based (Infrastructure as Code) → You define the full environment in a template file (YAML/JSON for CFT, HCL for Terraform).
- Slower to start since you must write the full infra definition before deploying.
- Best for repeatable, large-scale infrastructure provisioning.

2. AWS CLI & boto3
- Scripting-based → You directly run commands (CLI) or write Python scripts (boto3) to perform actions.
- Faster for quick tasks like creating a bucket, uploading a file, or stopping an EC2 instance.
- Best for automation, ad-hoc operations, and lightweight scripting.


3. 🚀 Why use boto3 over AWS CLI?
- Programming vs Commands
- AWS CLI → Just executes shell commands (one at a time). Good for  quick tasks.
- boto3 → Full Python SDK → You can write logic (loops, conditionals, error handling, retries, etc.). CLI can’t do that.
- Serverless (Lambda, etc.) → Lambda supports Python, so you can directly use boto3 inside your Lambda functions.

> Use AWS CLI → when you want quick, one-off commands.
> Use boto3 → when you need automation, logic, integration, or serverless apps (Lambda with Python).

---

# project using github codespace and boto3
## 1. launch s3 using boto3

step1: open codespace and in search bar search for <br>
> dev container

[image]()

<br><br>

now continue by modifying your active configuration.... <br>
[image]()

<br><br>

a new pop-up will be shown and select aws cli..<br>
[image]()

<br><br>


NOW TRY :  
> aws --version <br>
> if it gives command not found The feature didn’t actually get installed into your Codespace container. <br>
> You need to rebuild/restart your container for the changes to take effect.

## 1: Rebuild the container
Inside your Codespace (browser tab), press
- Ctrl + Shift + P (Windows/Linux)

A search bar (Command Palette) will appear at the top.

type: Rebuild Container
- Select it → wait while the container restarts and installs the new dev container features (like AWS CLI).

After it’s done, run:
aws --version

[image]()


## 2: create new file 

1. search boto3 documentation on google
2. in side bar go to Available services
3. search for s3
4. follow the command:
   
<br>

[follow this link to view entire code](https://github.com/SereneSyntax04/python-for-devops/blob/main/boto3/s3.py) 
[to delete the created bucked using python script, follow this link]()
