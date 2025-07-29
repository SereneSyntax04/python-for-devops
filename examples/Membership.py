# Membership Operators

'''
1️⃣ Using in with a List
 Aryan is checking if Meera is on the birthday guest list.'''
guest_list = ["Meera", "Neha", "Ravi"]

print("Meera" in guest_list)     # True
print("Sana" in guest_list)      # False

'''
2️⃣ Using not in with a List
 Meera wants to know who’s not on the list.'''
print("Aryan" not in guest_list)   # True
print("Neha" not in guest_list)    # False

'''
3️⃣ Using in with a String
 You’re checking if the word “cake” is in the party menu description.'''
menu = "The party will have pizza, drinks, and cake."

print("cake" in menu)         # True
print("burger" in menu)       # False

'''
4️⃣ Using in with a Tuple
 Aryan wants to know if his favorite number is in the lucky draw.'''
lucky_numbers = (7, 13, 21)

print(13 in lucky_numbers)     # True
print(5 in lucky_numbers)      # False


