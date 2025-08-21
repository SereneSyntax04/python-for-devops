# File Handling
File handling allows us to create, read, update, and delete files in Python.

## 1. Opening a File
```python
file = open("example.txt", "r")   # open in read mode
```
- "r" → read

- "w" → write (overwrites existing file)

- "a" → append (adds to end of file)

- "x" → create new file (error if exists)

- "b" → binary mode (images, pdf, etc.)

- "t" → text mode (default)


## 👉 Always close the file:
```python
file.close()
```


## 2. Reading Files
```python
# Read full file
data = file.read()

# Read one line
line = file.readline()

# Read all lines (list of strings)
lines = file.readlines()
```


## 3. Writing to Files
```python
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Second line.")
```

👉 "w" erases old content. <br>
👉 Use "a" to append instead:
```pyhton
with open("example.txt", "a") as file:
    file.write("\nAppended line.")
```



## 4. Checking if File Exists
```python
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")
```

## 5. Deleting Files
```python
import os
os.remove("example.txt")
```


---
# TASK:
Updates the value of a given key in a server configuration file. <br>
Example: MAX_CONNECTIONS=200  ->  MAX_CONNECTIONS=600 <br>


[refer this link for task](https://github.com/SereneSyntax04/python-for-devops/tree/main/examples/file)
