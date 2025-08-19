# TASK:
'''
** Get pull request information on a repository using python. **
    algorithm:
    requirement is to get pull request on a github repo, for that will need to write a python script.
    so basically will write a python script to interact with github repo (api)
    1. we need to identify module that we need and its: 'request' module. so install and import the module
    2. using the moule we need to make api call
    3. Any tool that we interact with gives result in JSON format so now we gotta convert this into dictionary format so python can interact with.
    4. print the required thing (pull request)
'''



# to check if a module is present or not : pip show <module name>

# pip  install requests (terminal)
import requests

'''
requests module in Python — it’s basically your go-gitto tool for working with HTTP in Python. 
Think of it as a way to talk to websites, APIs, or even your own backend servers without having to write raw socket code 
or manually format HTTP requests.


1. go to google and search github api docs
2. go to pull request section (since our task is based on pull request)
3. Code samples for "List pull requests" --  /repos/{owner}/{repo}/pulls
4. do the required chnages in this url
'''

#"https://api.github.com/repos/kubernetes/kubernetes/pulls"

'''
1. we replacced owner and repo with kubernetes cause thats the path for kubernetes repo in official kubernetes github , you can aslo google search kubernetes/kubernetes . 
2. just add 'https://api.github.com' at the very start and enclose everything inside double quotes and url is created.
3. now try to copy paste the url and you'll get the json document.
4. it was simple , just put the url in browser but through pyhton we have command : requests.get() '''

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls") # place the entire respone in variable named response.
''' using print to see what we fetched    
1. print(type(response))     we got object 
2. print(response.json())   trying to convert into dictionary format , .json() is used to internally convert the json doc into dictionary 
3. print(response.status_code)   200 
    so response is an object that request module returns.
    now when we use print(response.json()) we get a huge file that is not readable, so will store entire result in variable and reat what is at 1st index'''

complete_detail = response.json()

print(type(complete_detail))  # check it's type dict or list (if its dict, you hit the api limit try again afer 60 min.)


# this is for when type is list
'''
print(len(complete_detail))    # how many PRs are returned?
print(complete_detail[0]["id"])  # get the 'id' key , using [] since its list
print(complete_detail[2]["user"]["login"]) # nested dictionaries: ["user"] → inside that PR’s dictionary, there’s a "user" key. Its value is another dictionary (with details about the user who opened the PR). ["login"] → finally, this extracts the GitHub username of that user.
for i in range(len(complete_detail)):
    print(complete_detail[i]["user"]["login"])
'''
