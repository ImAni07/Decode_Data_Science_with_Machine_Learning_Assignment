"""
    Question No. - 15:
    Write a Python module named file_operations.py with functions for reading, writing, and appending data to a file.
"""

# This file consists of {file_operations.py}
# File operations module

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

def append_file(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data)

# Example usage
file_name = "example.txt"

# Write to the file
write_file(file_name, "Hello, world!\n")

# Append to the file
append_file(file_name, "This is appended data.\n")

# Read from the file
print("File content:")
print(read_file(file_name))

# Step-by-Step Process:
"""
    Step 1: Create a new file and name it {file_operations.py}
    Step 2: In {file_operations.py}, define functions for reading, writing, and appending data to files.
    Step 3: Save the File.
"""

# Sample Output:
"""
    File content:
    Hello, world!
    This is appended data.
"""