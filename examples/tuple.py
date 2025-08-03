my_tuple = (1, 2, 'apple', 'banana')

'''1️⃣ Tuple Indexing
Just like lists, indexing starts at 0.'''
first_element = my_tuple[0]  # → 1
print(first_element)

'''2️⃣ Tuple Length
Use len() to find the number of elements.'''
length = len(my_tuple)  # → 4
print(length)

'''3️⃣ Accessing Elements
Tuples can't be changed, but you can still access their values.'''
print(my_tuple[2])  # → 'apple'

'''4️⃣ Tuple Packing & Unpacking
Group values into a tuple (packing) and extract them (unpacking).'''
coordinates = (10.5, 20.3)
x, y = coordinates  # x → 10.5, y → 20.3
print(x,y)

'''5️⃣ Concatenating Tuples
Join two tuples to form a new one.'''
new_tuple = my_tuple + (3.14, 'cherry')
print(new_tuple)

'''6️⃣ Check for Membership
Use in to verify if a value exists in the tuple.'''
print('apple' in my_tuple)  # → True

'''7️⃣ Multiple Return Values from Functions
Functions can return tuples — handy for returning more than one value.'''
def get_credentials():
    return ('admin', 'password123')

user, password = get_credentials()
print(user, password)



print('\n')
# Tuples are great when returning structured data that shouldn't change:
def get_server_info():
    return ('192.168.0.1', 8080)

ip, port = get_server_info()
print(f"Connect to {ip} on port {port}")