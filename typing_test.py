import csv
import platform
import textwrap

# Module 1: platform
print("===== SYSTEM INFORMATION =====")
system_info = {
    "Operating System": platform.system(),
    "Computer Name": platform.node(),
    "Python Version": platform.python_version()
}

for key, value in system_info.items():
    print(f"{key}: {value}")

# Module 2: textwrap
print("\n===== SYSTEM DESCRIPTION =====")
description = "This program displays computer information and saves the details into a CSV file for easy viewing and organization."

formatted_text = textwrap.fill(description, width=50)
print(formatted_text)

# Module 3: csv
print("\n===== SAVING DATA =====")
with open("system_info.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Information", "Details"])

    for key, value in system_info.items():
        writer.writerow([key, value])

print("System information successfully saved to system_info.csv!")