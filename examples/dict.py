
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
