
<h3 align="center"> Steps to perform the task </h3>

## Step 1: Sign in to AWS Management Console
- Navigate to AWS Lambda service.


## Step 2: Create and Set Up a New Lambda Function  

### 1. Create Function  
- Click **Create function**.  
- Choose **Author from scratch**.  
- Provide:  
  - **Function name**  
  - **Runtime** (e.g., Python 3.9)  
  - **Execution role** (select an existing  role with proper permissions or create a new one).  
- Click **Create function**.  

### 2. Deploy the Code  
- In the **function editor**, you’ll see the default sample code AWS Lambda provides (usually a simple “Hello from Lambda” function).  
- For now, don’t change anything — we’ll just test this default code to confirm Lambda is working properly.  
- Click **Deploy** to save the function.  

### 3. Test the Function  
- Click **Test**.  
- Configure a test event (use a sample template or create your own JSON).  
- Run the test and verify the output.  


## Step 3: Configure CloudWatch Rule to Trigger Lambda  

1. **Create Rule**  
   - Go to **Amazon CloudWatch → Rules**.  
   - Click **Create rule**.  

2. **Define Event Source**  
   - Select **Event pattern** as the event source.  
   - Event type: **EBS volume notification**  
   - Specific event: **CreateVolume**  

3. **Set Target**  
   - Target: **Lambda function**  
   - Choose your Lambda function from the list.  

4. **Configure and Create Rule**  
   - Provide a **name** and optional **description** for the rule.  
   - Review the settings and click **Create rule**.  


## Step 4: Dummy Run (Verify CloudWatch → Lambda Integration)  

Before writing the actual code, we need to confirm that the CloudWatch event can successfully trigger the Lambda function.  

1. **Trigger an Event**  
   - Go to **EC2 → Volumes**.  
   - Create a **new EBS volume**.  

2. **Wait for Event Delivery**  
   - Wait for about a minute to allow the event to propagate.  

3. **Check Lambda Logs**  
   - Open your Lambda function in the AWS Console.  
   - Navigate to **Monitor → Logs in CloudWatch**.  
   - Check the **Log Stream** for a new entry/report.  

⚠️ Since our Lambda function currently doesn’t have any action defined, you should just see a **basic execution report** confirming the trigger worked.  


## Step 5: Write the Actual Lambda Code (Convert EBS Volume Type to gp3)

### Understanding the Lambda Function

```python
def lambda_handler(event, context):
```

- lambda_handler → This is the default function that gets triggered when Lambda runs.

- event → Contains all the details that CloudWatch sends to Lambda when an event occurs.

- context → Includes runtime information about the Lambda function itself (we won’t use it much here).


### Exploring the Event Data

To understand what’s inside the event, add a print statement:

```python
print(event)
```

Then:

1. Deploy the function.

2. Create a new EBS volume (this will trigger the Lambda again).

3. Go to CloudWatch → Log groups → your Lambda log stream.

4. You’ll see a JSON report of the event data. Copy that JSON and paste it into an online JSON formatter.

5. After formatting, you’ll get a clear dictionary-like structure of what CloudWatch sends to Lambda.

From that data, we’re mainly interested in this field:

```json
"resources": [
    "arn:aws:ec2:region:account-id:volume/vol-xxxxxxxxxxxx"
]
```

- This gives us the EBS Volume ID, which we’ll need to modify the volume type from gp2 → gp3 using boto3.

###  Write boto3 Code to Modify the Volume Type to gp3

Now that we know how to extract the **Volume ID** from the CloudWatch event, let’s write the actual code that updates the volume type using **boto3**.


### Extracting the Volume ID from the Event  

```python

import boto3
def get_volume_id_from_arn(volume_arn):
   arn_parts = volume_arn.split(':')
   volume_id = arn_parts[-1].split('/')[-1]
   return volume_id
```

Here, volume_arn is the resource part we got from the JSON formatter.

To pass this as input to the above function, use:

```python
volume_arn = event['resources'][0]
```

Explanation:

- event → contains all the data sent by CloudWatch.

- ['resources'] → extracts only the resources section.

- [0] → takes the first element (the EBS volume ARN).

Now call the function to retrieve the Volume ID:

```python
volume_id = get_volume_id_from_arn(volume_arn)
```

### Using boto3 to Modify the Volume Type

Referencing the official boto3 documentation for modify_volume, the required parameters are:

```python
response = ec2_client.modify_volume(
   VolumeId = volume_id ,
   VolumeType = 'gp3' ,
)
```

<b>To make this work, we first need to create an EC2 client: </b>

```python
ec2_client = boto3.client('ec2')
```
⚠️ Make sure this client creation line appears before the modify_volume() call.

### Final Cleanup and Deployment

Before deploying:

- Remove the print(event) and any unnecessary imports like json.

- Remove the default Lambda return statement (not needed here).

<b>Your final Lambda code should look like this: </b>
[image]
Now Deploy your function to save the changes.


## Step 6: Add Permissions to the IAM Role  

By default, the IAM role attached to your Lambda function **does not have permission** to modify or describe EBS volumes.  
We need to add those permissions manually.

### Steps to Add Permissions

1. Go to **IAM → Roles** in the AWS Console.  
2. Select the role attached to your Lambda function (e.g., `ebs_role`).  
3. Open the **Permissions** tab.  
4. Click **Add permissions → Create inline policy**.  

### Configure the Inline Policy
- **Service:** `EC2`  
- **Actions:**  
  - `DescribeVolumes`  
  - `ModifyVolume`  
- **Resources:**  
  - `All resources`  

Click **Next**, then:  
- **Review policy**  
- Name it: `ebs_volume_check`  
- Click **Create policy**


## Step 7: Verify Everything Works  

Now that all configurations are done — Lambda, CloudWatch, and IAM permissions — let’s validate that the automation is working as expected.

1. **Delete** any previously created test EBS volumes (to avoid confusion).  
2. **Create a new EBS volume** in the EC2 console — this will automatically trigger your Lambda function via CloudWatch.  
3. Go to **CloudWatch → Log groups → your Lambda log stream**, and open the **latest log stream**.  
   - Check for a successful execution message confirming the volume modification.  
4. Head back to the **EC2 Console → Volumes** section.  
   - Confirm that the **newly created volume type** has been automatically updated to **gp3**.  

✅ If the type shows as **gp3**, congratulations — your end-to-end automation (CloudWatch → Lambda → EC2) is working perfectly!



