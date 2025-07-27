# Assignment Operators

x = 5   # Basic Assignment

# Addition Assignment
y = 10
y += 3  # Equivalent to y = y + 3

'''Scene: Aryan and Meera are running a small cake business. 
They start with some cakes and keep updating their stock as sales happen. 
Let’s see how they use assignment operators to keep track!'''
# They start with:
aryan_cakes = 20
meera_cakes = 15

# They bake more cakes
aryan_cakes += 10       # Aryan bakes 10 more
meera_cakes += 5        # Meera bakes 5 more

print("After baking:")
print("Aryan:", aryan_cakes)      # 30
print("Meera:", meera_cakes)      # 20

# Aryan eats 2 cakes, Meera gives 3 to her friend
aryan_cakes -= 2
meera_cakes -= 3

print("\nAfter snacking and sharing:")
print("Aryan:", aryan_cakes)      # 28
print("Meera:", meera_cakes)      # 17

# A party order comes in: double the stock!
aryan_cakes *= 2
meera_cakes *= 2

print("\nAfter big order preparation:")
print("Aryan:", aryan_cakes)      # 56
print("Meera:", meera_cakes)      # 34

# They sell half of their cakes
aryan_cakes /= 2
meera_cakes /= 2

print("\nAfter selling half:")
print("Aryan:", aryan_cakes)      # 28.0
print("Meera:", meera_cakes)      # 17.0

# They box cakes in packs of 6
aryan_cakes %= 6
meera_cakes %= 6

print("\nLeftover cakes after packing in boxes of 6:")
print("Aryan:", aryan_cakes)      # 4.0
print("Meera:", meera_cakes)      # 5.0

# Aryan wants to go all out: cube his leftover cakes
aryan_cakes **= 3

print("\nAryan turns leftovers into cake tower:")
print("Aryan:", aryan_cakes)      # 64.0

print('\n')



# Task 2: Assignment Operators
'''Create a variable total and initialize it to 10.
Use assignment operators (+=, -=, *=, /=) to update the value of total.
Print the final value of total.'''

# Step 1: Initialize the variable
total = 10

# Step 2: Apply assignment operators
total += 5    # total = 10 + 5 → 15
total -= 3    # total = 15 - 3 → 12
total *= 2    # total = 12 * 2 → 24
total /= 4    # total = 24 / 4 → 6.0

# Step 3: Print the final result
print("Final value of total:", total)
