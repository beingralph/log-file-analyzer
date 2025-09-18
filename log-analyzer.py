import re
from collections import Counter

# Read log file
with open("sample.log", "r") as file:
    logs = file.readlines()

# Extract timestamps and errors using regex
timestamps = []
errors = []

for line in logs:
    match = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
    if match:
        timestamps.append(match.group())
    if "ERROR" in line or "FAIL" in line:
        errors.append(line.strip())

# Count error frequency
error_counts = Counter(errors)

# Display results
print("Unique Timestamps Found:", len(set(timestamps)))
print("\nErrors Summary:")
for error, count in error_counts.items():
    print(f"{error} --> {count} times")
