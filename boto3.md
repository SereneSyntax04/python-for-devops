<h1 align="center"> BOTO3:</h1>

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

<br>

<h1 align="center">  Project using Github CodeSpace and Boto3  ☁️ </h1>

<h2 align="center">🪣 Launch S3 using Boto3</h2>

## Step 1: Setup AWS CLI in Codespaces  

1. Open your Codespace and launch the **Command Palette**  
   - `Ctrl + Shift + P` (Windows/Linux)  <br>
   - `Cmd + Shift + P` (Mac)  <br>

2. Search for:  
   ``` dev container ``` <br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/70b15f08b0913fa7dafab663c02ea9cc79a2ed9b/images/boto_1.png" 
       alt="DevOps Project" 
       width="600"/>
</p>

   
3. select "Modify your active configuration…" <br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/70b15f08b0913fa7dafab663c02ea9cc79a2ed9b/images/boto_2.png" 
       alt="DevOps Project" 
       width="600"/>
</p>

   
4. From the pop-up, check ✅ AWS CLI <br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/70b15f08b0913fa7dafab663c02ea9cc79a2ed9b/images/boto_3.png" 
       alt="DevOps Project" 
       width="600"/>
</p>


<br><br>

## Step 2: Verify Installation

1. Run inside terminal:
```bash
aws --version
```
- ✅ Shows version → AWS CLI installed successfully.

- ❌ command not found → rebuild your container.

<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/70b15f08b0913fa7dafab663c02ea9cc79a2ed9b/images/boto_4.png" 
       alt="DevOps Project" 
       width="600"/>
</p>

 ## FIX THE ISSUE if facing 'command not found' : 
 How to rebuild

- Open Command Palette → search 'Rebuild Container'.
- Wait for Codespace to restart & install AWS CLI.
- Run again:
   ```
   aws --version
   ```

## Step 3: Configure AWS & Install Boto3

Now that AWS CLI is installed, configure it with your IAM credentials:

aws configure
 👉 Provide:

- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., ap-south-1)
- Output format (leave as json or table)

Then install boto3 (Python AWS SDK):
``` pip install boto3 ```


## Step 4: Write Python Script with Boto3

Go to the official [Boto3 Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
<p>
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_7.png" 
       alt="DevOps Project" 
       width="600"/>
</p>

In sidebar → Available Services → S3 

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_8.png" width="300" height="300"/><br>
      <sub>Step 1: Sidebar → Available Services</sub>
    </td>
    <td align="center">
      <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_9.png" width="300" height="300"/><br>
      <sub>Step 2: Select S3</sub>
    </td>
    <td align="center">
      <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_10.png" width="300" height="300"/><br>
      <sub>Step 3: Bucket Management Commands</sub>
    </td>
  </tr>
</table>


Check [create_bucket and other methods](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html)
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_11.png" width="500" height="500"/><br>
  <sub>Step 4: Select <b>CreateBucket</b> from the available command options</sub>
</p>
<br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_12.png" width="500" height="500"/><br>
  <sub>Step 5: Scroll to <b>Request Syntax</b> → Find required parameters & commands</sub>
</p>


Use them in your Python script

📄 Example scripts from this repo:

- [📝 Create S3 bucket](https://github.com/SereneSyntax04/python-for-devops/blob/main/boto3/s3.py)
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_13.png" width="500" height="500"/><br>
  <sub>Python script to create an S3 bucket using Boto3</sub>
</p>
<br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_14.png" width="500" height="500"/><br>
  <sub>AWS S3 Console → Bucket successfully created</sub>
</p>


- [🗑️ Delete S3 bucket](https://github.com/SereneSyntax04/python-for-devops/blob/main/boto3/s3delete.py)
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_15.png" width="500" height="500"/><br>
  <sub>Python script to delete an S3 bucket using Boto3</sub>
</p>
<br>
<p align="center">
  <img src="https://github.com/SereneSyntax04/python-for-devops/blob/e508351d81c5191e50dbb43766c74dbb6a14fbe0/images/boto_16.png" width="500" height="500"/><br>
  <sub>AWS S3 Console → Bucket no longer listed after deletion</sub>
</p>

---

### 📌 **Project Summary**  

**🚀 Project:** Using **Python & Boto3** in **GitHub Codespaces**  
**✅ Task:** Create and delete an **AWS S3 bucket** via Python scripts  
**🛠️ Skills demonstrated:** AWS CLI setup, credential configuration, Python scripting, S3 bucket management, verification in **AWS Console**

---
