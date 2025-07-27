
# Identity Operators 
'''When to Use
Comparing if two variables point to the same object (not just equal values).

Especially useful when working with mutable objects (like lists, dicts).

Can be used to check if something is None, like:
'''

if x is None:
    pass



#  With Integers (Immutable)
a = 5
b = 5

print(a is b)        # True – small integers are cached, same memory
print(a is not b)    # False
# Since integers are immutable and cached, both a and b point to the same object.


# With Lists (Mutable)
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)     # True – values are equal
print(x is y)     # False – different objects in memory
# The values of x and y are the same, but they're stored separately.


# Two variables referencing the same object
z = x
print(z is x)     # True – both point to the same list
# Now z and x are literally the same object.


#  Checking with None (Common Use)
temp = None

if temp is None:
    print("No value assigned yet.")
# This is the recommended way to check if a variable is None.
