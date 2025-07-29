# Examples of Logical Operators

'''
1️⃣ Logical AND (and)
You’ll go out only if it’s not raining and you have money.'''
is_raining = False  # change this value and see changes
have_money = True

if not is_raining and have_money:
    print("You go out for ice cream!")
else:
    print("You stay home.")

'''
2️⃣ Logical OR (or)
You’ll watch a movie if it’s Sunday or if you’re on leave.'''
is_sunday = False
on_leave = True

if is_sunday or on_leave:
    print("You watch a movie.")
else:
    print("No movie today.")

'''

3️⃣ Logical NOT (not)
You’ll take an umbrella only if it’s not sunny.'''
is_sunny = False

if not is_sunny:
    print("You take an umbrella.")
else:
    print("No umbrella needed.")





# Combo Example
age = 18
has_id = True

if age >= 18 and has_id:
    print("Access granted.")
else:
    print("Access denied.")

