def update_server_config(file_path, key, value):
    """
    Updates the value of a given key in a server configuration file.
    Example: MAX_CONNECTIONS=200  ->  MAX_CONNECTIONS=600
    """

    # Step 1: Read the existing content of the server configuration file
    # We use readlines() to get a list of all lines for easy iteration
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Step 2: Open the file in write mode ('w') to overwrite it with updated content
    with open(file_path, 'w') as file:
        for line in lines:
            # Step 3: Check if the line contains the key we want to update
            # Using 'if key in line' → this is a simple match, but note:
            # It may also match partial strings like "MAX_CONNECTIONS_TIMEOUT"
            if key in line:
                # Step 4: If key is found, write a new line with updated value
                # Format: key=value
                file.write(key + "=" + value + "\n")
            else:
                # Step 5: If it's not the target key, keep the original line
                file.write(line)


# Path to the server configuration file
server_config_file = '/workspaces/python-for-devops/examples/file/server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'   # The setting we want to modify
new_value = '600'                   # New maximum connections allowed

# Step 6: Call the function to perform the update
update_server_config(server_config_file, key_to_update, new_value)


# run this file and go check in server.conf if max_connection is changed or not.