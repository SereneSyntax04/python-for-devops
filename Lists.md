# Understanding Lists and List Data Structure in Python
🧾 What is a List?
A list is a built-in data structure in Python used to store multiple items in a single variable.

Lists are:
- Ordered → items maintain the order in which they were added.
- Mutable → you can modify them (add, remove, or change elements).
- Flexible → can contain mixed data types (numbers, strings, booleans, etc).

🧠 Think of it as a shopping bag holding different items.
```python
my_list = [1, 2, 3, 'apple', 'banana']
```


---

## Mini Use-Case
You could use a list to store:

1. Running services
2. IP addresses in a subnet
3. Log lines matching a pattern
4. Packages to be installed on a VM
```python
packages = ['nginx', 'docker', 'git']
if 'docker' in packages:
    print("Docker already installed.")
```

[Example](https://github.com/SereneSyntax04/python-for-devops/blob/main/examples/list.py)




---

## Using Lists and File Handling to Explore Folders in Python
When you start programming, understanding how to organize and manage multiple pieces of data is key. One of the most useful tools for this in Python is the list — a flexible container that holds items in order and lets you easily add, remove, or check things.

In real-world programs, lists help handle everything from user inputs to file management. Below, we’ll explore the basics of lists and then see how they power a small program that lets you check the contents of multiple folders on your computer — handling errors smoothly and keeping the code neat.

[Example](https://github.com/SereneSyntax04/python-for-devops/blob/main/examples/listfile.py) <br>
**Code Explanation** <br>
1. Importing the os Module <br>
The program starts by importing Python’s built-in os module, which provides functions to interact with the operating system. Here, it’s used to list the files inside folders.

2. Defining list_files_in_folder(folder_path) <br>
This function takes a folder path as input and tries to get the list of files in that folder using os.listdir().
- If successful, it returns the list of files and None for the error message.
- If the folder doesn’t exist (FileNotFoundError) or access is denied (PermissionError), it returns None for files and a corresponding error message.

3. Defining main() <br>
The program asks the user to enter multiple folder paths separated by spaces.
- It splits this input into a list of individual folder paths.
- For each folder path in the list, it calls list_files_in_folder() to get the files or an error message.
- If files are found, it prints them one by one. Otherwise, it prints the error.

4. Running the Script <br>
The line if __name__ == "__main__": ensures that main() runs only when the script is executed directly, not when imported into another module.
