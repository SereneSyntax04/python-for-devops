# FUNCTION, MODULE, PACKAGE

## 1️⃣ Functions — The "Reusable Recipe" of Python
A function is like a recipe card. You write it once and reuse it whenever you need. It can take ingredients (arguments) and give you a dish (return value).

```python
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

👉 Why use functions?

- Saves time (no repeating code)
- Makes code easier to read
- Helps you debug easily

---

## 2️⃣ Modules — Your Personal Toolkit
A module is just a .py file with reusable code like functions, variables, or classes. You write your logic once and import it wherever needed.
```pyhton
# my_module.py
def square(x):
    return x ** 2

pi = 3.14159265
```
**You can use it like this in another file:**
```python
import my_module

print(my_module.square(5))  # Output: 25
print(my_module.pi)         # Output: 3.14159265
```

👉 Why use modules?

- Keeps code organized
- Makes collaboration easier
- Helps reuse your work in other projects

---

## 3️⃣ Packages — Your Code Library
A package is a folder with a bunch of related modules inside it. 
It has a special __init__.py file that says, "Hey Python, this is a package!"
```pyhton
my_package/
    __init__.py
    module1.py
    module2.py
```
**You can import modules like this:**
```python
from my_package import module1

module1.function_from_module1()
```
👉 Why use packages?

- Perfect for big projects
- Helps manage large codebases
- Makes your project easy to navigate



