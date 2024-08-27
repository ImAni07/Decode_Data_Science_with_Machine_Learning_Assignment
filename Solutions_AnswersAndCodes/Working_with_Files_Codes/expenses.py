"""
    Question No. - 18:
    Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent on various expenses listed in the file.
"""
# Creating 'expenses.txt' file

import csv

def generate_expenses():
    expenses = [
        "Date,Description,Amount\n",
        "2024-01-15,Office Supplies,12050.00\n",
        "2024-01-20,Software Licenses,3200.00\n",
        "2024-02-10,Employee Training,15000.00\n",
        "2024-03-05,Travel Expenses,45000.00\n",
        "2024-03-15,Utilities,2000.00\n"
    ]
    return ''.join(expenses)

def write_expenses_file():
    with open('expenses.txt', 'w') as file:
        file.write(generate_expenses())

write_expenses_file()

# Calculating total expenses from expenses.txt

total_expenses = 0

with open('expenses.txt', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        try:
            expense = float(row[2])
            total_expenses += expense
        except ValueError:
            print(f"Skipping invalid number: {row[2]}")

print(f"Total expenses: {total_expenses}")

# Step-by-Step Process:-
"""
    Step 1: Create a new Python Script
    Step 2: If there's not any 'expenses.txt' file, then create one, as in this case, it has been created.
    Step 3: Open and read the file, converting each line to a float.
    Step 4: Accumulate the total expenses by summing the values read from the file.
    Step 5: Print the total amount spent.
    Step 6: Save the script.
"""

# Output:-
# Total expenses: 77250.0