"""Task: Write receipt.py that:

Asks the user for a store name, an item name, and its price (as a string for now — no math required yet)
Prints a formatted receipt using what you know about print():
================================
        SHOP RITE
================================
Item:       Laptop
Price:      $1200.00
--------------------------------
Thank you for shopping with us!
================================
Requirements:

Use print("=" * 32) for separator lines
Use end="" at least once to control line endings
Use sep at least once
Use an f-string for at least one line
The store name must be cleaned (stripped, title-cased) from user input
Use escape characters if needed (e.g., if the store name contains a quote)"""

# Ask user for store name, item name and item price
store_name = input("Enter Store Name: ").strip().upper()
item_name = input("Enter Item Name: ").strip().title()
item_price = input("Enter Item Price: ").strip()

WIDTH = 32

# Print Receipt
print("=" * WIDTH)
print(f"{store_name.center(WIDTH)}")
print("=" * WIDTH)
print(f"Item:       {item_name}")
print(f"Price:      ${item_price}")
print("-" * WIDTH)
print("Thank you for shopping with us!", end="\n" + "=" * WIDTH)
