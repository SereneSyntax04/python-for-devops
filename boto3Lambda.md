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