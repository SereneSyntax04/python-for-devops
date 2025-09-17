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

### Q: If there's a script that needs to run every day at 10 AM for 15 minutes, what approach should you use — EC2 or Lambda, and why?

**Answer:**  
The best approach is to use **AWS Lambda** with an **EventBridge (CloudWatch Events) schedule**. Lambda can run for up to 15 minutes, which matches the script’s requirement, and it eliminates the need to manage any servers. With EC2, you would have to launch an instance daily, run the script, and then terminate it to avoid unnecessary costs. Forgetting to stop the instance could result in paying for idle time, and overall it adds more operational overhead.  

By using Lambda, you get a fully **serverless, automated, and cost-efficient** solution. You pay only for the actual execution time, and scaling is handled automatically if you need to run multiple scripts in parallel in the future. This makes Lambda with EventBridge the most practical and reliable option for scheduled tasks of 15 minutes or less.  

---

## 5. Best usecase of serverless architecture

#### 1. Cost Optimization
Serverless platforms like AWS Lambda follow a **pay-as-you-go** model.  
- You are only billed for the compute time when your code is executed.  
- No costs are incurred for idle resources.  
- This makes Lambda highly cost-efficient, especially for workloads with variable or unpredictable traffic.  

#### 2. Compliance and Security
Serverless functions can help organizations enforce **governance, compliance, and security policies** by automating checks and responses.  

**Example Use Case:**  
Suppose an organization has a policy that **no one should create an EBS volume of type `gp2`** (since `gp3` is cheaper and recommended).  
- A developer mistakenly creates a `gp2` volume.  
- A scheduled **Lambda function** can run every day at 10 AM to:  
  1. Identify if there are any `gp2` volumes.  
  2. If found, trigger an **SNS notification** to alert the management or compliance team.  

This ensures compliance by continuously monitoring the environment and notifying stakeholders whenever a violation occurs.


---
<br><br><br>


<h2 align="center"> Compliance and Security Automation with AWS Lambda </h2>
📌 Scenario

Organizations running workloads on AWS need to follow governance and compliance policies to avoid unnecessary costs, security loopholes, or non-standard resource usage. However, developers may accidentally create resources that don’t comply with organizational policies (e.g., using outdated EBS volume types, enabling public S3 buckets, or provisioning non-approved instance types).

As a Cloud Engineering team, our responsibility is to:

- Continuously monitor the AWS environment.

- Enforce compliance with organizational policies.

- Automate responses to violations to reduce manual overhead.

This project demonstrates how **AWS Lambda** combined with **CloudWatch Events (EventBridge)** can be used to detect non-compliant resources and take corrective actions.

### 🎯 Goal

- Automate compliance checks in AWS.

- Detect non-compliant resources (e.g., EBS gp2 volumes).

- Alert the compliance/security team via SNS.

- Optionally fix issues automatically (e.g., convert gp2 → gp3).

Extend the same approach to EBS, RDS, EC2, S3, and EKS.


<p align="center">
  <img src="reference" 
       alt="reference" 
       width="600"/>
</p>
