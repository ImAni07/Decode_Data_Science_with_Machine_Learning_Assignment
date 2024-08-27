"""
    Question No. - 19:
    Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent on various expenses listed in the file.
"""

# Creating a 'paragraph.txt' file

def generate_paragraph():
    paragraph = (
        "Python is a powerful and versatile programming language that is widely used in many fields, "
        "including web development, data science, and automation. Its simple syntax and readability make "
        "it an ideal choice for both beginners and experienced developers. Python supports various programming "
        "paradigms, including procedural, object-oriented, and functional programming. The language has a rich "
        "standard library and a vibrant community that contributes to a vast ecosystem of third-party packages and "
        "tools. Whether you are working on a small script or a large-scale application, Python's flexibility and "
        "ease of use make it a valuable asset in any developer's toolkit."
    )
    return paragraph

def write_paragraph_file():
    with open('paragraph.txt', 'w') as file:
        file.write(generate_paragraph())

write_paragraph_file()

# Counting word occurrences in paragraph.txt

from collections import Counter

with open('paragraph.txt', 'r') as file:
    words = file.read().lower().split()

word_count = Counter(words)

for word in sorted(word_count):
    print(f"{word}: {word_count[word]}")

# Step-by-Step Process:-
"""
    Step 1: Create a new Python Script.
    Step 2: Create a 'paragraph.txt' file, if it does not exists.
    Step 3: Open 'paragraph.txt' in read mode, convert text to lowercase, and split it into words.
    Step 4: Use 'Counter' from the 'collections' module to count occurrences of each word.
    Step 5: Print each word and its count in alphabetical order.
    Step 6: Save the file.
"""

# Sample Output:-
"""
    a: 7
    an: 1
    and: 8
    any: 1
    application,: 1
    are: 1
    asset: 1
    automation.: 1
    beginners: 1
    both: 1
    choice: 1
    community: 1
    contributes: 1
    data: 1
    developer's: 1
    developers.: 1
    development,: 1
    ease: 1
    ecosystem: 1
    experienced: 1
    fields,: 1
    flexibility: 1
    for: 1
    functional: 1
    has: 1
    ideal: 1
    in: 2
    including: 2
    is: 2
    it: 2
    its: 1
    language: 2
    large-scale: 1
    library: 1
    make: 2
    many: 1
    object-oriented,: 1
    of: 2
    on: 1
    or: 1
    packages: 1
    paradigms,: 1
    powerful: 1
    procedural,: 1
    programming: 2
    programming.: 1
    python: 2
    python's: 1
    readability: 1
    rich: 1
    science,: 1
    script: 1
    simple: 1
    small: 1
    standard: 1
    supports: 1
    syntax: 1
    that: 2
    the: 1
    third-party: 1
    to: 1
    toolkit.: 1
    tools.: 1
    use: 1
    used: 1
    valuable: 1
    various: 1
    vast: 1
    versatile: 1
    vibrant: 1
    web: 1
    whether: 1
    widely: 1
    working: 1
    you: 1
"""