
# 🔀 **Conditional Statements in Python – Making Decisions in Code**

Conditional statements help your code **make decisions**. You can tell Python:

> “If this is true, do that. Otherwise, do something else.”

Python uses:

* `if`
* `elif` (short for **else if**)
* `else`

to handle different scenarios based on conditions.

---

### 🔹 **`if` Statement**

* Checks a condition.
* Runs the code **only if** the condition is `True`.

🧠 Think of it like:

> "If it’s raining, carry an umbrella."

```python
if condition:
    # Do this if condition is True
```

---

### 🔹 **`elif` Statement**

* Comes after an `if`.
* Lets you check **another condition** if the first one was False.
* You can stack **multiple** `elif` blocks.

🧠 Like:

> "If it’s not raining but cloudy, wear a jacket."

```python
if condition1:
    # Run this
elif condition2:
    # Run this instead
```

---

### 🔹 **`else` Statement**

* Runs if **none** of the `if` or `elif` conditions are `True`.
* It’s the **fallback/default** action.

🧠 Like:

> "If it’s not raining or cloudy, wear sunglasses."

```python
if condition:
    # True block
else:
    # Fallback block
```

---

### 🧠 Quick Memory Trick

> 🧩 **if → elif → else** <br>
> Keep asking “what if…” until nothing fits — then use `else`.


[Examples](https://github.com/SereneSyntax04/python-for-devops/blob/main/examples/Conditional.py)
