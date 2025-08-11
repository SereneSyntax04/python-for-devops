# Loops in Python (for and while)

Loops are a fundamental concept in programming, allowing you to perform repetitive tasks efficiently.
In Python, there are two primary types of loops: for and while.

---

## For Loop
The for loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a set of statements for each item in the sequence.
The loop continues until all items have been processed.

Syntax:
```python
for variable in sequence:
    # Code to be executed for each item
```

---

## While Loop
The while loop continues to execute a block of code as long as a specified condition is True.
It’s useful when you don’t know in advance how many times to run the loop.

Syntax:
```pyhton
while condition:
    # Code to be executed as long as condition is true
```

---

# Loop Control Statements
Loop control statements allow you to modify loop execution flow.
Python provides break and continue for this purpose.

---

## break Statement
Exits the loop immediately when a condition is met.
Example:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)
```

---

## continue Statement
Skips the current iteration and moves to the next one.
Example:
```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)
```


[Example]()
