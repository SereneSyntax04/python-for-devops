# Dictionary holding server configurations
# Each server has its own nested dictionary with keys: ip, port, and status
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Function to retrieve the status of a given server
# - server_name: string key like 'server1', 'server2', etc.
# - Uses .get() to avoid KeyErrors if server_name doesn't exist
# - Returns the status if found, otherwise "Server not found"
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage of the function
# Asking for the status of 'server2'
server_name = 'server2'
status = get_server_status(server_name)

# Print the result in a readable format
print(f"{server_name} status: {status}")