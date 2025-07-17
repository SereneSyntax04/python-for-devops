'''
DevOps Scenario (Question):
In a DevOps environment, you often deal with configuration management of web servers — like setting server names, ports, HTTPS status, and maximum allowed connections. 
How can you define server configuration as global variables, print them for verification, and later update those configurations dynamically during 
runtime to reflect changes like switching ports or disabling HTTPS?
'''


# Web server config variables (global variable)
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

def server_info():
    # Print config
    print(f"Server Name: {server_name}")
    print(f"Port: {port}")
    print(f"HTTPS Enabled: {is_https_enabled}")
    print(f"Max Connections: {max_connections}")

server_info()   #calling function
print('\n')

# Update config
port = 443
is_https_enabled = False

# Print updated config
server_info() #calling function

'''
The given Python code defines server configuration as global variables and uses a function server_info() to display them. 
Initially, it prints the default configuration. 
Afterward, some values like port and is_https_enabled are updated, and the function is called again to reflect these changes. 
This demonstrates how configuration values can be easily managed and updated at runtime, which is a common practice in DevOps for flexibility and environment adaptability.
'''
