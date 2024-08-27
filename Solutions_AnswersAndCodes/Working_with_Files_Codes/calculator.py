"""
    Question No. - 12:
    Write a Python module named calculator.py containing functions for addition, subtraction, multiplication, and division.
"""

# This file consist of a Module named {calculator.py}
# Calculator Module

# Calculator module

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# Printing Output

import calculator

print("Calculator Module")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition: ", calculator.add(num1, num2))
print("Subtraction: ", calculator.subtract(num1, num2))
print("Multiplication: ", calculator.multiply(num1, num2))

try:
    print("Division: ", calculator.divide(num1, num2))
except ValueError as e:
    print("Error: ", e)

# Sample Output:
"""
    Calculator Module
    Enter first number: 7.0
    Enter second number: 45.0
    Addition:  52.0
    Subtraction:  -38.0
    Multiplication:  315.0
    Division:  0.15555555555555556
"""

# Step-by-Step Process:
"""
    Step 1: Create a new file and name it {calculator.py}
    Step 2: In {calculator.py}, define functions for addition, subtraction, multiplication, and division. Implement error handling for division by zero.
    Step 3: Save the File.
"""