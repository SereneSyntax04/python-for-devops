'''
                    Day 2 
So this exercise is regrading inbuilt function that we will perform on different data types.

Scenario 1:     
In your DevOps work , you have 1000 of arn (arn of IAM user) and you gotta submit only the username from those piles of arn
here's how you can use python to get only the names out of  arn 
'''

arn = "arn:aws:iam::123456789012:user/john" #this is using only one arn but for 1000, we store those arn in dictionary and then apply these below code
print(arn.split("/"))
print(arn.split("/") [1])   #using split (inbuiltfunction) which creates a new list with two items and we want username that is at 1 index

information = "this is trial. String is used as an example. To use split function"  #using simple split() function with condition as dot(.) to separate sentence
word = information.split(".")
print("short sentences in string: " , word)   

print("\n")

'''
Scenario 2:    
now you had bunch of different errors and warnings but you just want to focus on certain errors , using python:
'''

    

