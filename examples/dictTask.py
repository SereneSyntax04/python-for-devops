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




# pip  install requests (terminal)
import requests

'''
requests module in Python — it’s basically your go-to tool for working with HTTP in Python. 
Think of it as a way to talk to websites, APIs, or even your own backend servers without having to write raw socket code 
or manually format HTTP requests.
'''

# go to google and search github api docs
# go to pull request (since our task is based on pull request)
# Code samples for "List pull requests" --  /repos/{owner}/{repo}/pulls

"api.github.com/repos/kubernetes/kubernetes/pulls"
#we replacced owner and repo with kubernetes cause thats the path for kubernetes repo in official kubernetes github , you can aslo google search kubernetes/kubernetes 
# just add 'api.github.com' at the very start and enclose everything inside double quotes and url is created
print('hello')