                                                # this is command line argument
# Command-line Arguments are usually used to pass input values like filenames, numbers, or operation types needed for that specific run.
# Command-line Arguments can be visible in process lists (ps command) or shell history, so not recommended for sensitive information.
import sys  # Importing the sys module to access command-line arguments



# Check if user provided enough arguments (at least 2 after the script name)
if len(sys.argv) < 2:    # sys.argv[0] is the script name, next args are actual inputs
    print("Please provide your name as an argument.")
    sys.exit()  # Exit the program if not enough arguments are passed

# Combine the first and second command-line arguments into a full name
name = sys.argv[1] + " " + sys.argv[2]  # sys.argv[1] = first name, sys.argv[2] = last name
# Greet the user using f-string formatting
print(f"Hello, {name}!")
'''
python env.py Shrushti Shrivastav
Output: Hello, Shrushti Shrivastav!
'''



# simple calculator feature using command-line arguments
def add(num1,num2):
    return num1 + num2   # Function to add two numbers

# Get the numbers and operation from command-line arguments
num1 = int(sys.argv[3]) # Third argument (index 3) is the first number (as previous two arguments are used for name)
operation = sys.argv[4] # Fourth argument (index 4) is the operation (e.g., "add")
num2 = int(sys.argv[5]) # Fifth argument (index 5) is the second number

# Perform the operation if it's "add"
if operation == "add":
    output = add(num1,num2)
    print(output)   # Print the result of the addition
'''
Example usage:
python env.py shrushti shrivastav 2 add 3

Explanation of command-line args:
- sys.argv[1] = "shrushti" (first name)
- sys.argv[2] = "shrivastav" (last name)
- sys.argv[3] = 2 (num1)
- sys.argv[4] = "add" (operation)
- sys.argv[5] = 3 (num2)

Expected Output:
5
'''





# TASK :  Create a Python command-line calculator that takes two numbers and an operation (add, sub, mul, div) as arguments and prints the result.
# import sys   :Import sys module to handle command-line arguments

# Define arithmetic functions
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2

# First, check if we received at least 6 arguments (script + name + 2 numbers + operation)
if len(sys.argv) < 6:
    print("Usage: python env.py <first_name> <last_name> <num1> <operation> <num2>")
    sys.exit()

# Read inputs from command-line arguments
name = sys.argv[1] + " " + sys.argv[2]
num1 = int(sys.argv[3])
operation = sys.argv[4].lower()  # Make it case-insensitive (e.g., "Add", "ADD", "add")
num2 = int(sys.argv[5])

# Perform the operation based on user input
if operation == "add":
    result = add(num1, num2)
elif operation == "sub":
    result = sub(num1, num2)
elif operation == "mul":
    result = mul(num1, num2)
elif operation == "div":
    result = div(num1, num2)
else:
    result = "Unsupported operation. Use: add, sub, mul, or div."

# Print greeting and result
print(f"Result: {result}")

'''
Example usage:
python env.py Shrushti Shrivastav 10 sub 3

Output:
Hello, Shrushti Shrivastav!
Result: 7

Supported operations:
- add => addition
- sub => subtraction
- mul => multiplication
- div => division (with zero check)
'''





                                                # this is environment variable

# Environment Variables are often used to store sensitive data like API keys, passwords, or config settings, because they don’t need to be hardcoded in the script.
# Environment Variables are hidden from the command-line history and output, making them safer for storing secrets.

import os
print(os.getenv("pass"))
'''
export pass="shru12"
python env.py   
'''
