
#Loop Practice Examples for DevOps

#1️⃣ Iterate over server list
#Loop through a list of server hostnames and print a "checking status" message.

servers = ['app1','cache001','db01']
for server in servers:
    print(f"checking status of {server}...")

print('\n')


# 2️⃣ Find failed jobs in CI logs
ci_logs = [
    "Job #101: SUCCESS",
    "Job #102: FAILED",
    "Job #103: SUCCESS",
    "Job #104: FAILED",
]

for log in ci_logs: # 1st iteration → "Job #101: SUCCESS" ; 2nd iteration → "Job #102: FAILED" AND SO ON
    if 'FAILED' in log: #The in keyword checks if the substring "FAILED" appears anywhere inside log , "FAILED" in "Job #102: FAILED" → ✅ True, "FAILED" in "Job #101: SUCCESS" → ❌ False
        print(f"Alert !! : {log}")

print('\n')



# 3️⃣ Retry until success (while loop)
attempt = 1
max_attempts = 5

while attempt <= max_attempts:  #This means keep looping as long as the number of attempts is less than or equal to 5.
    print(f"Attempt {attempt}: Connecting to server...")    #This just tells us which attempt number we’re on.
    # simulate a failure until attempt 3
    if attempt == 3:            #You’re pretending the connection fails on attempts 1 and 2. When attempt becomes 3, the connection is “successful” 
        print("✅ Connection established!") #— you print the success message and then 
        break   #break stops the loop immediately.
    attempt += 1    #If the connection wasn’t successful, you add 1 to attempt and try again.

print('\n')




# 4️⃣ Skip maintenance servers
servers = ["app01", "app02-maintenance", "db01"]

for server in servers:
    if "maintenance" in server: #The in keyword here checks whether "maintenance" appears anywhere in the server name. 
        continue    #If it does, you hit continue — which skips the rest of the code for this iteration and jumps to the next item in the loop.
    print(f"Deploying to {server}...")  #So "app02-maintenance" is skipped entirely.

print('\n')




# 5️⃣ Disk space check
disk_usages = [45, 72, 88, 50]  # in %
for usage in disk_usages:
    if usage > 80:
        print(f"⚠️ High disk usage: {usage}%")
