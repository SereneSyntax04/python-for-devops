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

