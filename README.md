# Python for DevOps

[1.     🛠️ Shell Scripting vs Python – Choosing the Right Tool in DevOps](https://github.com/SereneSyntax04/python-for-devops/blob/main/shellVSpython.md#-when-to-use-shell-scripting)

[2.     🧱 Data Types – The Building Blocks of Code](https://github.com/SereneSyntax04/python-for-devops/blob/main/datatypes.md)

[3.     📚 Keywords & Variables – Naming and Defining Your Code’s World](https://github.com/SereneSyntax04/python-for-devops/blob/main/keywordVar.md)

[4.     📝 Functions, Modules & Packages – Writing Clean and Reusable Code](https://github.com/SereneSyntax04/python-for-devops/blob/main/function.md)

[5.     🖥️ CLI Arguments & Environment Variables – Making Code Configurable](https://github.com/SereneSyntax04/python-for-devops/blob/main/args.md)

[6.     🧠 Operators in Python – The Characters Running Your Code’s Drama](https://github.com/SereneSyntax04/python-for-devops/tree/main/operator)

[7.     🔀 Conditional Statements – Making Decisions in Code](https://github.com/SereneSyntax04/python-for-devops/blob/main/Conditional.md)

[8.     🎯 Tuples – Immutable Collections of Data](https://github.com/SereneSyntax04/python-for-devops/blob/main/tuple.md) 

[9.     📋 Lists – Dynamic and Flexible Collections](https://github.com/SereneSyntax04/python-for-devops/blob/main/Lists.md)

[10.     🔁 Loops in Python – Automating Repetition](https://github.com/SereneSyntax04/python-for-devops/blob/main/loops.md)

[11.    📖 Dictionaries – Mapping Keys to Values](https://github.com/SereneSyntax04/python-for-devops/blob/main/dict.md)

[12.    📑 File Handling – Working with Files in Python](https://github.com/SereneSyntax04/python-for-devops/blob/main/file.md)

[13.    ☁️ Boto3 with AWS – Automating Cloud Resources (Theory + Project)](https://github.com/SereneSyntax04/python-for-devops/blob/main/boto3.md)


---


[🔑 Core Responsibilities of a DevOps Engineer ](https://github.com/SereneSyntax04/python-for-devops/blob/main/responsibilities.md)

[Examples folder for demo](https://github.com/SereneSyntax04/python-for-devops/tree/main/examples)


---


<h1 align="center">🔧 Syncing GitHub Codespace with Remote Repository</h1>

If you’ve created or edited a `.md` file directly on **GitHub**, your **Codespace** won’t automatically update to reflect those changes.  
Follow these steps to manually sync your Codespace:

---

## 🪜 Step-by-Step Guide

### **Step 1: Open the Codespace Terminal**
- In your Codespace, press **`Ctrl + `** (backtick) to open the integrated terminal.


### **Step 2: Pull the Latest Changes**
Run the following command to fetch and merge updates from your remote repository:

```bash
git pull origin main
```
This command ensures that any changes (like a newly created .md file) made directly on GitHub are synced to your Codespace.


### **Step 3: Merging a New Branch (Optional)**
If you are working with a newly created branch and want to merge its updates into the main branch, use:

```bash
git pull --no-rebase
```
This merges changes without rebasing, keeping your commit history clean when syncing between branches in Codespaces.


### **✅ Result**
After running these commands, your Codespace will be up-to-date with all the latest changes made on GitHub.