"""
    Question No. - 13:
    Implement a Python package structure for a project named ecommerce, containing modules for product management and order processing.
"""

# This is the __init__ file of ecommerce

# Initialization file for the ecommerce package

# This file can be empty, but it is essential for Python to recognize the directory as a package.

# Author: Anirban Majumder
# Date: 26th August, 2024

"""
    Directory Structure:
    ecommerce/
    __init__.py
    product_management.py
    order_processing.py
"""

"""
    Implement a Python Package Structure for a Project named 'ecommerce':
    
        The Step-by-Step process for the same has been described below:
        
            Step 1:- Create Package Directory: Create a new directory named 'ecommerce'.
            
            Step 2:- Add Initialization File: Inside the 'ecommerce' directory,
            create a file named '__init__.py'.
            This file can be empty but is necessary for Python to recognize the directory as a package.
            
            Step 3:- Create Module:
                i. Add two new files inside the 'ecommerce' directory.
                    a. 'product_management.py'
                    b. 'order_processing.py'
                ii. Implement functionality related to product management and order processing in these files.
            
            Step 4:- Save the Files: Save all files to complete the package structure.
"""

"""
# Sample Usage:

from ecommerce.product_management import add_product, update_stock, get_product_info
from ecommerce.order_processing import create_order, cancel_order

# Add a product
product = add_product("Apple Watch", 500, 10)

# Update stock
product = update_stock(product, 5)

# Get product info
print(get_product_info(product))  # Output: Product: Apple Watch, Price: 500, Stock: 15

# Create an order
print(create_order(product, 3))  # Output: Order placed for 3 units of Apple Watch.

# Cancel an order
print(cancel_order(product, 2))  # Output: Order for 2 units of Apple Watch has been canceled.

# Sample Output:
    Product: Apple Watch, Price: 500, Stock: 15
    Order placed for 3 units of Apple Watch.
    Order for 2 units of Apple Watch has been canceled.
"""