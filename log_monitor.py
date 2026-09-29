import re
import time

# Comprinno Tevico sarkha log monitor
LOG_FILE = "server.log"

# Sample log create 
with open(LOG_FILE, "w") as f:
    f.write("INFO: Server started\n")
    f.write("ERROR: Database connection failed\n")
    f.write("INFO: User login\n")
    f.write("ERROR: High CPU usage 90%\n")

print("--- Cloud Log Analyzer Started (Tevico Style) ---")

with open(LOG_FILE, "r") as file:
    for line in file:
        if "ERROR" in line:
            print(f"🚨 ALERT DETECTED: {line.strip()}")
            # Yethe email/SMS alert trigger
            # print("Sending alert to admin...")

print("\nMonitoring complete. Total errors logged to cloud.")
