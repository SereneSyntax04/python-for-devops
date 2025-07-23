# 🖥️ Command-Line Arguments 

## 1. What are Command-Line Arguments?
- Inputs passed directly from the terminal when running a Python script.
- Allow you to make scripts dynamic and reusable, instead of hardcoding values.

## 2. How to Access Them in Python?
- Using sys.argv (Basic way)
- sys.argv is a list that stores command-line arguments.
- Comes from Python's built-in sys module.
- Always starts with the script name at index 0.
```python
import sys

# Example: python deploy.py production server01

print(f"Script Name: {sys.argv[0]}")   # deploy.py
print(f"Environment: {sys.argv[1]}")   # production
print(f"Server Name: {sys.argv[2]}")   # server01
```

## Python sys Module
- sys is a built-in Python module that gives you access to system-level operations — things related to the Python interpreter itself.
- It's super useful for automating tasks, handling command-line arguments, controlling program exit, and managing standard I/O.
- Although `sys` is a built-in module in Python, you still need to **import it explicitly** using `import sys` before using its features, as it's part of the Python standard library stored within the Python installation.


## 3. ✅ What happens if no arguments are given?
- You’ll get an IndexError if you try to access sys.argv[1] when nothing was passed.
- Always validate the input before using it!
```python
if len(sys.argv) < 3:
    print("❌ Usage: python deploy.py <environment> <server_name>")
    sys.exit(1)
```

##  Why Do DevOps Engineers Use This?
1. Automates manual input during deployments or monitoring
2. Easy integration with scripts used in Jenkins, GitHub Actions, Ansible, etc.
3. Keeps scripts flexible across different servers/environments

---

# 🌍 Environment Variable (env var) 
An environment variable is a key-value pair stored in the operating system that can be used by programs or scripts to get config info like:

API keys, DB credentials, File paths, Runtime settings, Secrets or tokens

1️⃣ Why use env vars?
- Keeps sensitive data out of your code (like passwords)
- Lets the same script behave differently in dev, test, or prod
- Makes your apps portable and configurable

2️⃣ Common Use in DevOps
- Configure Docker containers
- Set AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
- Manage CI/CD pipeline variables (like in GitHub Actions, Jenkins)
