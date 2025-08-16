
'''
Keys must be unique and immutable.
Values can be any Python object.
Access time is fast because dictionaries use hash tables.
'''


# Basic Syntax and operations

my_dict = {
    "name": "Shrushti",
    "age": 21,
    "skills": ["Python", "AWS", "DevOps"]
}
# Accessing Values
print(my_dict)
print(my_dict["name"])

#  Adding & Updating
my_dict["location"] = 'India'
print(my_dict["location"])

# Removing Items
my_dict.pop("location")
print(my_dict)
# del my_dict["location"] # Removes 'location'
#my_dict.clear()         # Removes everything

print('\n')
# Looping Through a Dictionary
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(f"{key} → {value}")







# TASK:
'''
Get pull request information on a repository using python
    algorithm:
    requirement is to get pull request on a github repo, for that will need to write a python script.
    so basically will write a python script to interact with github repo (api)
    1. we need to identify module that we need and its: 'request' module.
    2. using the moule we need to make api call
    3. Any tool that we interact with gives result in JSON format so now we gotta convert this into dictionary format so python can interact with.
    4. print the required thing (pull request)
'''

print('hello')