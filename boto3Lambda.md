<h2 align="center"> AWS Lambda </h1>

## 1. What is AWS Lambda?
- **AWS Lambda** is a *serverless compute service* provided by AWS.  
- You run your code (functions) without provisioning or managing servers.  
- Pay only for:
  - Number of requests
  - Execution time (duration in ms)
- AWS Lambda removes the need for server management by automatically scaling code execution on demand, making it cost-efficient and ideal for event-driven or unpredictable workloads.


## 2. Compute Models: EC2 vs Lambda

| Feature          | **EC2 (Traditional Compute)**                       | **Lambda (Serverless Compute)**         |
|------------------|------------------------------------------------------|------------------------------------------|
| **Server Mgmt**  | You provision, configure, patch, and monitor VMs     | AWS fully manages servers (invisible to you) |
| **Scaling**      | Manual or Auto Scaling (slow, instance-based)        | Auto-scales instantly (per request)       |
| **Cost Model**   | Pay for uptime (per second/hour), even if idle       | Pay only per request & execution time     |
| **Use Cases**    | Long-running apps, databases, monolithic workloads   | Event-driven tasks, microservices, automation |
| **Language**     | Any (via AMI/containers)                             | Supports multiple runtimes (Python, Node, Go, etc.) |



## 4. What is "Serverless"?
- A cloud model where:
  - You focus only on writing code/business logic.  
  - No need to manage servers, scaling, or infrastructure.  
- *Serverless ≠ no servers* → It means **servers are abstracted away** (AWS manages them).  

Examples of serverless services:
- AWS Lambda (compute)
- DynamoDB (database)
- S3 (storage)



## 5. How DevOps Engineers Use Lambda
- **Automation**:
  - Trigger scripts on S3 file upload, EC2 state change, or CloudWatch event.  
  - Example: Run Python code to resize images when uploaded to S3.  

- **CI/CD Pipelines**:
  - Integrate with CodePipeline/CodeBuild for deployments.  
  - Example: Run automated post-deployment checks.  

- **Monitoring & Alerts**:
  - Process CloudWatch logs and send alerts to Slack/Teams.  

- **Infrastructure Ops**:
  - Auto-start/stop EC2 instances on schedule (cost optimization).  
  
- **Security**:
  - Auto-remediate security issues (close open ports, rotate keys).  



