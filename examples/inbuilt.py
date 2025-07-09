'''
                    Day 2 
So this is regrading inbuilt function that we will perform on different data types
imagine a scenario in your DevOps work , you have 1000 of arn (arn of IAM user) and you gotta submit only the username from those piles of arn
here's how you can use python  
'''

arn = "arn:aws:iam::123456789012:user/john"
print(arn.split("/"))
print(arn.split("/") [1])   #using split (inbuiltfunction) which creates a new list with two items and we want username that is at 1 index