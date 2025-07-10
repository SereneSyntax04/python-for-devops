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

mistakes = '400 Bad Request , 401 Unauthorized, 404 Not Found, 408 Request Timeout, 502 Bad Gateway, 504 Gateway Timeout'
major_issue = '404 Not Found'   #this is a substring that we created to find out if this specific error(character) is present or not in our variable named mistakes.
if major_issue in mistakes:
    print("Major issue:", major_issue)

print("\n")

'''
Scenario 3:
just trying out some inbuilt functions ..you never know, you might just need them
'''
text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

text = "Python is awesome"
length = len(text)
print("Length of the string:", length)

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)


print("\n")
print("\n")


# Integer variables
num1 = 10
num2 = 5

# Integer Division
result1 = num1 // num2
print("Integer Division:", result1)

# Modulus (Remainder)
result2 = num1 % num2
print("Modulus (Remainder):", result2)

# Absolute Value
result3 = abs(-7)
print("Absolute Value:", result3)


print("\n")
print("\n")


# Float variables
num1 = 5.0
num2 = 2.5

# Basic Arithmetic
result1 = num1 + num2
print("Addition:", result1)

result2 = num1 - num2
print("Subtraction:", result2)

result3 = num1 * num2
print("Multiplication:", result3)

result4 = num1 / num2
print("Division:", result4)

# Rounding
result5 = round(3.14159265359, 4)  # Rounds to 4 decimal places
print("Rounded:", result5)


print("\n")
print("\n")


'''
Scenario 2:    
now you had bunch of different errors and warnings but you just want to focus on certain errors , using python:
'''
#regex
import re

mistakes = '400 Bad Request , 401 Unauthorized, 404 Not Found, 408 Request Timeout, 502 Bad Gateway, 504 Gateway Timeout'
pattern = r"404 Not Found"
patterns = r"400 Bad Request"

search = re.search(pattern, mistakes)
if search:
    print("Error found:", search.group())
else:
    print("Pattern not found")


match = re.match(patterns, mistakes)
if match:
    print("Match found:", match.group())
else:
    print("No match")


replacement = "403 Forbidden"
new_text = re.sub(patterns, replacement, mistakes)
print("Modified text:", new_text)


pattern = r","
split_result = re.split(pattern, mistakes)
print("Split result:", split_result)
print(split_result[2])
