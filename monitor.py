import psutil

# This part fetches the RAM details from your laptop
memory = psutil.virtual_memory()

print("--- Dell Laptop Health Report ---")
print(f"Total RAM: {memory.total / (1024**3):.2f} GB")
print(f"RAM Currently Used: {memory.percent}%")

# DevOps logic: alerting if resources are low
if memory.percent > 80:
    print("ALERT: RAM usage is high! Close some Chrome tabs.")
else:
    print("Status: System health is stable.")
    