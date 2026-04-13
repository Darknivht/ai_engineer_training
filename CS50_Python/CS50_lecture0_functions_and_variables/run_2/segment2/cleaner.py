"""Task: Write cleaner.py that:

Asks the user for their full name (first and last)
Intentionally works even with messy input (extra spaces, wrong capitalization)
Prints the cleaned version"""

# Ask user for their name
full_name = input("Enter your full name: ")

# Print original user input
print(full_name)

# print Clean user input
print(full_name.strip().title())