
my_list = [1, 2, 3, 'apple', 'banana']

'''1️⃣ Indexing (Accessing Elements)
List indices start from 0.'''
first_item = my_list[0]  # → 1
print(first_item)

'''2️⃣ List Length
Use len() to get how many items are in the list.'''
length = len(my_list)  # → 5
print(length)

'''3️⃣ Appending Elements
Add new items to the end using append().'''
my_list.append(4)  # my_list → [1, 2, 3, 'apple', 'banana', 4]
print(my_list)

'''4️⃣ Removing Elements
Remove an item by value with remove().'''
my_list.remove('apple')  # → Removes the first occurrence of 'apple'
print(my_list)

'''5️⃣ Slicing Lists
Create a sub-list from the original list using slicing.'''
subset = my_list[1:4]  # → elements from index 1 to 3
print(subset)

'''6️⃣ Concatenating Lists
Combine two or more lists using +.'''
combined = my_list + [5, 6]  # → joins both lists
print(combined)

'''7️⃣ Sorting a List
Use sort() to sort numeric or alphabetical lists.'''
numbers = [3, 1, 2]
numbers.sort()  # → [1, 2, 3]
print(numbers)

'''8️⃣ Check Membership
Use in to check if a value exists in the list.'''
is_present = 'banana' in my_list  # → True
print(is_present)


print('\n')
# list usecase:
packages = ['nginx', 'docker', 'git']
if 'docker' in packages:
    print("Docker already installed.")