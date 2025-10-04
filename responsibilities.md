<h1 align="center"> AWS Lambda </h1>

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


## 3. What is "Serverless"?
- A cloud model where:
  - You focus only on writing code/business logic.  
  - No need to manage servers, scaling, or infrastructure.  
- *Serverless ≠ no servers* → It means **servers are abstracted away** (AWS manages them).  

Examples of serverless services:
- AWS Lambda (compute)
- DynamoDB (database)
- S3 (storage)


## 4. How DevOps Engineers Use Lambda

DevOps engineers use AWS Lambda extensively to automate and simplify cloud operations. <br>
1. It can trigger scripts based on events such as S3 file uploads, EC2 state changes, or CloudWatch alarms—for example, resizing images automatically when they are uploaded to S3. 
2. Lambda also integrates into CI/CD pipelines with services like CodePipeline and CodeBuild, enabling automated checks after deployments. 
3. For monitoring, it processes CloudWatch logs and can send alerts directly to collaboration tools like Slack or Microsoft Teams. 
4. In infrastructure management, Lambda helps optimize costs by automatically starting or stopping EC2 instances on a schedule. 
5. It is also valuable for security, where it can automatically remediate issues such as closing open ports or rotating keys. 
<br> Overall, Lambda gives DevOps engineers a serverless, event-driven way to handle automation, monitoring, infrastructure, and security with minimal overhead.



---

<h1 align="center"> 🔑 Core Responsibilities of a DevOps Engineer </h1> <br> 
 Every DevOps engineer generally deals with two major tasks: <br>
 
### 1. Compliance & Security Automation – Ensuring the AWS environment follows organizational policies and remains secure.
### 2. Cost Optimization – Making sure cloud resources are used efficiently and costs are minimized.

---










<br><br>

<h1 align="center"> Compliance and Security Automation with AWS Lambda </h1>
(foundational, cloudwatch + lambda, serverless approach, compliance and security automation)

### Q: If there's a script that needs to run every day at 10 AM for 15 minutes, what approach should you use — EC2 or Lambda, and why?

**Answer:**  
The best approach is to use **AWS Lambda** with an **EventBridge (CloudWatch Events) schedule**. Lambda can run for up to 15 minutes, which matches the script’s requirement, and it eliminates the need to manage any servers. With EC2, you would have to launch an instance daily, run the script, and then terminate it to avoid unnecessary costs. Forgetting to stop the instance could result in paying for idle time, and overall it adds more operational overhead.  

By using Lambda, you get a fully **serverless, automated, and cost-efficient** solution. You pay only for the actual execution time, and scaling is handled automatically if you need to run multiple scripts in parallel in the future. This makes Lambda with EventBridge the most practical and reliable option for scheduled tasks of 15 minutes or less.  

---

<h2 align="center"> TASK : Compliance and Security Automation with AWS Lambda </h2>

📌 Scenario

Organizations running workloads on AWS need to follow governance and compliance policies to avoid unnecessary costs, security loopholes, or non-standard resource usage. However, developers may accidentally create resources that don’t comply with organizational policies (e.g., using outdated EBS volume types, enabling public S3 buckets, or provisioning non-approved instance types).

As a Cloud Engineering team, our responsibility is to:

- Continuously monitor the AWS environment.
- Enforce compliance with organizational policies.
- Automate responses to violations to reduce manual overhead.

This project demonstrates how AWS Lambda combined with CloudWatch Events (EventBridge) can be used to detect non-compliant resources and take corrective actions.

> This approach can be extended to EBS, RDS, EC2, S3, EKS, and other AWS services.

⚙️ [Step-by-Step Guide: Complete AWS Lambda Compliance Project]()



---







<br><br>

<h1 align="center"> Cost Optimization </h1>
(foundational, cloudwatch + lambda, cost optimization)

### Q: If there are old EBS snapshots that are no longer linked to any active EC2 instance, what’s the best way to ensure they don’t keep incurring unnecessary storage costs — manual cleanup, EC2 script, or Lambda?

**Answer:**
The best approach is to use AWS Lambda with an EventBridge (CloudWatch Events) schedule. Lambda can be set to run daily, automatically scanning for stale EBS snapshots and deleting them if they are not associated with any active instances.

This eliminates the need to manage servers (as you would with EC2), avoids human error from manual cleanup, and ensures cost efficiency. With Lambda, you only pay for the execution time, making it a serverless, automated, and cost-effective solution for recurring cleanup tasks.

---

<h2 align="center"> TASK : Cost Optimization </h2>

### 📌 Scenario

In cloud environments, cost often creeps in when engineers forget to clean up unused resources.

For example:

- A company had an EC2 instance with an external EBS volume to store sensitive data and config files.
- Daily snapshots (backups) of that EBS volume were taken for data protection.
- Later, the EC2 instance was deleted after data migration.
- But the attached EBS volume and its snapshots were not deleted.

Result: AWS continues charging for unused storage and snapshot retention, leading to unnecessary costs.

As DevOps/Cloud Engineers, it’s our responsibility to avoid wasteful spending by identifying such unused resources and removing them safely.

### As a DevOps/Cloud Engineering team, our responsibility is to:

- Continuously monitor the AWS environment for unused or stale resources.
- Optimize storage and compute costs by cleaning up what’s no longer needed.
- Automate responses to reduce manual effort and prevent human oversight.

This project demonstrates how AWS Lambda combined with CloudWatch Events (EventBridge) can be used to identify unused or stale resources (such as EBS snapshots that are no longer attached to any instance) and automatically clean them up to reduce unnecessary AWS costs.

⚙️ [Step-by-Step Implementation: Automating EBS Snapshot Cleanup with Lambda]()