"""
    Question No. - 16:
    Write a Python program to create a text file named "employees.txt" and write the details of employees, including their name, age, and salary, into the file
"""

# Creating and writing to a file named employees.txt

import csv

employees = [
    {"name": "Anirban Majumder", "age": 24, "salary": 80000},
    {"name": "Nitin Bhardwaj", "age": 24, "salary": 80000},
    {"name": "Shaimak Shukla", "age": 27, "salary": 70000},
    {"name": "Kislay Chaturvedi", "age": 24, "salary": 70000},
    {"name": "Sanjay Sharma", "age": 27, "salary": 60000},
    {"name": "Nitin Patial", "age": 25, "salary": 60000}
]

with open('employees.txt', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'age', 'salary'])
    writer.writeheader()
    writer.writerows(employees)

# Step-by-Step Process:
"""
    Step 1: Create a new Python Script.
    Step 2: In the newly created Python Script, define a list of dictionaries containing employee details.
    Step 3: Open 'employees.txt' in write-mode and write employees details to the text file.
    Step 4: Save the file.
"""

# Output:
# The required text file is generated.