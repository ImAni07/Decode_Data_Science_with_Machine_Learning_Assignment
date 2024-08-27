"""
    Question No. - 14:
    Implement a Python module named string_utils.py containing functions for string manipulation, such as reversing and capitalizing strings.
"""

# This file consists of {string_utils.py}

# String utilities module

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    return s.capitalize()

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

# Test the functions
if __name__ == "__main__":
    input_string = "hello world"
    
    print("Original String: ", input_string)
    print("Reversed String: ", reverse_string(input_string))
    print("Capitalized String: ", capitalize_string(input_string))
    print("Uppercase String: ", to_uppercase(input_string))
    print("Lowercase String: ", to_lowercase(input_string))

# Step-by-Step Process:
"""
    Step 1: Create a new file and name it {string_utils.py}
    Step 2: In {string_utils.py}, define functions for string manipulation, including reversing and capitalizing strings.
    Step 3: Save the File.
"""


# Sample Output:
"""
    Original String:  hello world
    Reversed String:  dlrow olleh
    Capitalized String:  Hello world
    Uppercase String:  HELLO WORLD
    Lowercase String:  hello world
"""