# this is command line argument
import sys

# Check if user provided a name
if len(sys.argv) < 2:
    print("Please provide your name as an argument.")
    sys.exit()

name = sys.argv[1]
print(f"Hello, {name}!")

'''
python env.py Shrushti
'''




# this is environment variable
import os
print(os.getenv("pass"))
'''
export pass="shru12"
python env.py   
'''
