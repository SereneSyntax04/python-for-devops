# 1️⃣ Check if a server is reachable (ping-like check)
response_time = 120  # in ms

if response_time < 100:
    print("Server is super fast.")
elif response_time < 200:
    print("Server is okay.")
else:
    print("Server is slow or unresponsive.")

print('\n')


# 2️⃣ Check disk usage
disk_usage = 85  # in percentage

if disk_usage > 90:
    print("Critical: Disk almost full!")
elif disk_usage > 70:
    print("Warning: Disk usage high.")
else:
    print("Disk status normal.")

print('\n')


# 3️⃣ Validate environment before deployment
env = "production"

if env == "production":
    print("Deploy with caution!")
elif env == "staging":
    print("Safe to deploy for testing.")
else:
    print("Probably a dev machine.")

print('\n')


# 4️⃣ Determine if a service should restart
service_status = "failed"

if service_status == "active":
    print("Service is running fine.")
elif service_status == "inactive":
    print("Service is stopped. Start it.")
else:
    print("Service crashed. Restarting...")

print('\n')


# 5️⃣ Simple uptime-based load balancing
uptime = 4  # in hours

if uptime < 1:
    print("Server just restarted, avoid traffic.")
elif uptime < 24:
    print("Server is warm, good for handling load.")
else:
    print("Consider restarting for patching.")
