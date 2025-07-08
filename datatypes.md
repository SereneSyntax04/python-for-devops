# DataTypes: 

# 🧠 What Are Data Types?

Imagine every value in Python is like an item in your backpack. To stay organized, Python puts a label on each item: this one’s a number, that one’s a word, this one’s a list of things, etc.
These labels are called data types—and they tell Python what it can do with the item.

Let’s go on a tour of the Python Data Types Park 🎡👇

---

🔍 5 Quick Facts About Data Types in Python

🔄 Python figures out the type for you <br>
You don’t need to say int x = 5. Just write x = 5, and Python knows it’s an integer. That’s called dynamic typing.

🧱 Everything is an object <br>
Whether it’s a number, list, or string, it’s actually an object with built-in functions (called methods). <br>
→ Example: "hello".upper() gives "HELLO".

🔓 Mutable vs 🔒 Immutable

list, dict, set → Mutable (can change)

int, str, tuple → Immutable (can’t change)

🕵️‍♂️ Check data type with type() <br>
Use type(x) to find out what kind of data a variable holds. <br>
→ Example: type(3.14) → <class 'float'>

🔁 You can convert between types <br>
Want to turn "123" into a number? Just do int("123"). <br>
Python makes type casting super easy.

---
# Python Data Types

## 🎯 1. Numeric Data Types: The Number Zone
Used for counting, calculating, or handling precise values.

- int → Whole numbers <br>
> x = 10  # like how many apples you have 🍎

- float → Decimal numbers <br>
> y = 3.14  # price of one apple ₹

- complex → Real + imaginary numbers (rarely needed unless you’re doing heavy math) <br>
> z = 2 + 3j

- Math operations you can do: <br>
+, -, *, /, // (floor division), % (modulus), ** (power)

- Watch out: floating-point rounding issues (e.g., 0.1 + 0.2 != 0.3 exactly) <br>
Use abs(), round(), or Python’s math module for advanced math.


## ✉️ 2. Sequence Types: The Ordered Stuff
These are containers that hold things in a specific order.

- str → Text (string of characters) <br>
> name = "Shrushti"

- list → Changeable list of items <br>
> colors = ["red", "green", "blue"] <br>
> (You can add/remove items anytime)

- tuple → Fixed list of items <br>
> days = ("Mon", "Tue", "Wed") <br>
> (Set in stone — no changes allowed 📅)


## 🔐 3. Mapping Type: The Organizer

- dict → Dictionary with keys + values
> student = {"name": "Ravi", "age": 20}

Think of it like a contact list — each key points to a value.


## 🎲 4. Set Types: The Unique Collector

- set → Unordered collection, no duplicates
> nums = {1, 2, 3}

- frozenset → Like a set but immutable (cannot change)
> f_nums = frozenset([1, 2, 3]) <br>
> Use these when order doesn’t matter, but uniqueness does 💎


## 🔘 5. Boolean Type: True or False

- bool → Only two values: True or False
> is_logged_in = True <br>
> It’s like a yes/no switch


## 📦 6. Binary Types: Byte-Level Stuff
Used in advanced stuff like file handling, networking, etc.

- bytes → Read-only binary data
> data = b'hello' <br>

- bytearray → Editable binary data
> data = bytearray(b'hello')


## 🕳️ 7. NoneType: The Empty Box

- None → Means “no value here” or “empty”
> result = None <br>
> Useful as a placeholder when you’re waiting for a value later (like an empty form 📝).

