"""
    Question No. - 13:
    Implement a Python package structure for a project named ecommerce, containing modules for product management and order processing.
"""

# Product management module

def add_product(product_name, price, stock):
    return {"name": product_name, "price": price, "stock": stock}

def update_stock(product, amount):
    product['stock'] += amount
    return product

def get_product_info(product):
    return f"Product: {product['name']}, Price: {product['price']}, Stock: {product['stock']}"

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
"""
    Product: Apple Watch, Price: 500, Stock: 15
    Order placed for 3 units of Apple Watch.
    Order for 2 units of Apple Watch has been canceled.
"""