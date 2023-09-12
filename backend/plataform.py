import platform

# Get the operating system name
os_name = platform.system()

# Get the operating system version
os_version = platform.release()

# Get the detailed system information
system_info = platform.uname()

# Results
print(f"Operating System: {os_name}\n")
print(f"Operating System Version: {os_version}\n")
print(f"System Information: {system_info}")
