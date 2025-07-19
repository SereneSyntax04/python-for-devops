'''Write a Python function using match-case to perform basic arithmetic operations.
What will the function return when dividing 4 by 2 using the given operation?'''
def calculate(num1,num2,option):
    match option:
        case "+":
            res = num1 + num2
            return res
        case "-":
            res = num1 - num2
            return res
        case "*":
            res = num1 * num2
            return res
        case "/":
            res = num1 / num2
            return res
        case "":    # If no valid option is provided, return error message
            return "Invalid Option !"
       
print(calculate(4,2,"/"))

'''The given function calculate() takes two numbers and an operation symbol, 
then uses Python's match-case to select the correct arithmetic operation: addition, subtraction, multiplication, or division. 
If the operator doesn't match any case, it returns "Invalid Option !". 
When called with 4, 2, "/", it performs division and returns 2.0.'''



'''
import boto3

def create_basic_resources(bucket_name):
    # Create S3 Bucket
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f"S3 Bucket '{bucket_name}' created.")

    # Launch EC2 Instance
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId='ami-0c02fb55956c7d316',  # Example AMI (Amazon Linux 2)
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1
    )
    print(f"EC2 Instance launched with ID: {instance[0].id}")

# Example call
create_basic_resources('my-first-devops-demo-bucket-123')


# Helps you understand:
# ➡️ "One function = One task done automatically"

# When you call create_basic_resources(), it: 1.Creates one S3 bucket, 2.Launches one EC2 instance

'''