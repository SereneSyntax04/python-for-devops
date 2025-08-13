# List all the files in folders that user provide:
import os

def list_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folder_paths = input("Enter a list of folder paths separated by spaces: ").split() # using split to convert string into list
    
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)
        if files:
            print(f"Files in {folder_path}:")
            for file in files:
                print(file)
        else:
            print(f"Error in {folder_path}: {error_message}")

if __name__ == "__main__":
    main()



# enter userinput: /opt /tmp /xyz 
    # here /opt and /tmp are valid folders while /xyz is not , as per the requirement we entered the folder names separated by space


'''
1. Imports: We bring in Python’s os module, which lets us interact with the operating system — like listing files, checking paths, etc.

2. The list_files_in_folder function:
* Purpose: Take a folder path, try to list all the files in it, and handle errors gracefully.
* os.listdir(folder_path) → returns a list of all files and subfolders inside the given folder.
* Error handling:
a) If the folder doesn’t exist → catch FileNotFoundError and return an error message.
b) If the folder exists but you don’t have access → catch PermissionError.
* The function returns a tuple:
a) (files, None) if successful.
b) (None, "error message") if there’s an error.

3. The main function:
* Asks the user to enter multiple folder paths in one line (separated by spaces). .split() breaks the string into a list
* Loops through each folder path from the list. Calls the earlier function to get (files, error_message).
* If files is not empty, it prints the folder path and lists every file inside it.
* If files is None, it means something went wrong, so it prints the error message.

4. The if __name__ == "__main__": part
This makes sure main() runs only if you run this script directly, not if it’s imported somewhere else.
'''






'''
In Short
1. Ask the user for folder paths.

2. For each folder:
    Try to list files.
    If successful → print them.
    If error → print why it failed.
'''
