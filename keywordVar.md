# Python Keywords & Variables

## 📚 Keywords in Python
Keywords are like the “grammar rules” of Python. They have special meanings and you can’t use them as variable names. Python treats them seriously. They’re case-sensitive, so if is valid, but If is not.

Some commonly used keywords:
| Keyword                      | What it does               | Example                         |
| ---------------------------- | -------------------------- | ------------------------------- |
| `and`                        | Logical AND                | `if a > 0 and b > 0:`           |
| `or`                         | Logical OR                 | `if a == 0 or b == 0:`          |
| `not`                        | Logical NOT                | `if not is_valid:`              |
| `if`                         | Starts a condition         | `if x > 5:`                     |
| `else`                       | Defines fallback           | `else:`                         |
| `elif`                       | Else-if condition          | `elif x == 5:`                  |
| `while`                      | Loop until condition fails | `while count < 10:`             |
| `for`                        | Loop over a sequence       | `for item in list:`             |
| `in`                         | Membership check           | `if 'a' in word:`               |
| `try` / `except` / `finally` | Error handling             | `try: ... except: ... finally:` |
| `def`                        | Define function            | `def greet():`                  |
| `return`                     | Exit a function with value | `return "Hi"`                   |
| `class`                      | Define a class             | `class Car:`                    |
| `import`                     | Import modules             | `import math`                   |
| `from`                       | Import specific part       | `from math import pi`           |
| `as`                         | Alias a module             | `import numpy as np`            |
| `True` / `False`             | Boolean values             | `is_valid = True`               |
| `None`                       | Null value                 | `result = None`                 |
| `is`                         | Identity check             | `if a is b:`                    |
| `lambda`                     | Anonymous function         | `lambda x: x + 1`               |
| `with`                       | Context management         | `with open('file.txt') as f:`   |
| `global` / `nonlocal`        | Scope modifiers            | `global count`                  |


---

## 🎯 Understanding Variables in Python
A variable is like a labeled box where you store stuff.
You give it a name, put something inside it, and you can reuse it later.
```python
my_variable = 42
print(my_variable)  # Output: 42
```

## 🗺️ Variable Scope & Lifetime
- Local Scope: Variables inside a function.
- Global Scope: Variables defined outside functions.

```python
def my_function():
    x = 10  # Local variable
    print(x)

y = 20  # Global variable

def another_function():
    print(y)  # Accessing global

my_function()
another_function()
```
**Variable Lifetime**: 
- The lifetime of a variable is determined by when it is created and when it is destroyed or goes out of scope.
- Local variables disappear after the function ends. Global ones stick around till the program ends.

## ✨ Variable Naming Best Practices
✅ Make names clear and meaningful <br>
✅ Use snake_case (like_this) <br>
❌ Don’t use keywords as variable names <br>
❌ Don’t use one-letter names unless in loops <br>

```python
# Good example
user_name = "John"

# Bad example
class = "Python"  # ❌ Error! Reserved word

# Better clarity
a = 10          # ❓ Not clear
num_of_students = 10  # ✅ Much better
```


---

In DevOps or coding in general, understanding variables and keywords is like learning how to speak Python's language fluently.


[**Click here to visit more examples**](https://github.com/SereneSyntax04/python-for-devops/blob/main/examples/var.py)
