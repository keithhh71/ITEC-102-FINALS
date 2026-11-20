A Python module is a file or library that contains code we can use in a program.
Modules help us add features without writing everything ourselves.

This folder documents the three modules used in the System Information Saver:
1. Platform
2. OS
3. CSV

----------------------------------------
1. PLATFORM MODULE
----------------------------------------

Purpose:
Platform is a built-in Python module used to retrieve information about the computer's operating system, device name, and Python version.

How it is used in the System Information Saver:
Platform collects the computer's system information, including its operating system, computer name, and installed Python version. The collected data is stored in a dictionary and displayed on the screen.

Code:
    import platform

    system_info = {
        "Operating System": platform.system(),
        "Computer Name": platform.node(),
        "Python Version": platform.python_version()
    }

    for key, value in system_info.items():
        print(f"{key}: {value}")

Explanation:
- import platform loads the Platform module.
- platform.system() identifies the operating system, such as Windows or Linux.
- platform.node() returns the computer's network name or hostname.
- platform.python_version() returns the installed Python version.
- system_info stores the collected information in key-value pairs.
- system_info.items() allows the program to access each key and value.
- print() displays the system information on the screen.

Other uses:
The Platform module can also identify the machine architecture, processor information, platform details, and other system-related information.

Installation:
No installation is needed. The Platform module is included with Python.

----------------------------------------
2. OS MODULE
----------------------------------------

Purpose:
OS is a built-in Python module used to interact with the operating system. It allows a program to manage folders, check files, and work with file paths.

How it is used in the System Information Saver:
The OS module checks if the system_reports folder already exists. If it does not exist, the program creates it. It also prepares the file path where the CSV file will be saved.

Code:
    import os

    folder_name = "system_reports"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, "system_info.csv")

    print("Save location:", file_path)

Explanation:
- import os loads the OS module.
- folder_name stores the name of the folder where the report will be saved.
- os.path.exists() checks whether the folder already exists.
- os.makedirs() creates the folder if it is not yet available.
- os.path.join() combines the folder name and file name into a file path.
- file_path stores the final location of the CSV file.

Other uses:
The OS module can create, rename, and remove folders, check file locations, list files inside directories, and interact with certain operating system functions.

Installation:
No installation is needed. The OS module is included with Python.

----------------------------------------
3. CSV MODULE
----------------------------------------

Purpose:
CSV stands for Comma-Separated Values. It is a built-in Python module used to read and write data in a tabular format that can be opened in spreadsheet applications.

How it is used in the System Information Saver:
The CSV module saves the collected computer information into a file named system_info.csv. It organizes the information into two columns: Information and Details.

Code:
    import csv

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["Information", "Details"])

        for key, value in system_info.items():
            writer.writerow([key, value])

    print("System information saved successfully!")

Explanation:
- import csv loads the CSV module.
- open() creates or opens the CSV file using the specified file path.
- "w" means write mode, which creates a file or overwrites its contents if it already exists.
- newline="" helps prevent unwanted blank lines when writing CSV files.
- encoding="utf-8" allows the file to handle text properly.
- csv.writer(file) creates a writer object that writes data into the CSV file.
- writer.writerow() writes a single row of data.
- system_info.items() retrieves the stored system information.
- The for loop writes each system detail into the file.

Other uses:
The CSV module can store student records, grades, survey results, inventory lists, attendance records, and other tabular data.

Installation:
No installation is needed. The CSV module is included with Python.

----------------------------------------
SUMMARY
----------------------------------------

Platform - Collects computer information such as OS, computer name, and Python version.

OS - Manages the folder and file location.

CSV - Saves and organizes the collected information into a file.

Together, these three modules allow the program to collect, manage, and save computer information automatically.