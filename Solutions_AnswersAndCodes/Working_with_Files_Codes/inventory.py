"""
    Question No. - 17:
    Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays the contents of the file line by line.
"""
# Create a Text File

def generate_inventory():
    inventory = [
        "ID,Item,Quantity\n",
        "001,Laptop,50\n",
        "002,Mouse,150\n",
        "003,Keyboard,100\n",
        "004,Monitor,75\n",
        "005,Printer,20\n"
    ]
    return ''.join(inventory)

def write_inventory_file():
    with open('inventory.txt', 'w') as file:
        file.write(generate_inventory())

write_inventory_file()

# Reading contents of inventory.txt line by line

with open('inventory.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Step-by-Step Process:-
"""
    Step 1: Create a new Python Script.
    Step 2: If there is no pre-existing 'inventory.txt', then create one, just like it is created here, in this case.
    Step 3: Open 'inventory.txt' in read mode and iterate through each line.
    Step 4: Display File Contents.
    Step 5: Save the File.
"""

# Output:-
"""
    ID,Item,Quantity
    001,Laptop,50
    002,Mouse,150
    003,Keyboard,100
    004,Monitor,75
    005,Printer,20
"""