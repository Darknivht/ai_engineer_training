"""Task: Ask the user for their full name (first and last in one prompt). Use the .split() method to assign the first name and last name to two different variables on the same line (just like David Malan showed). Finally, use an f-string to print: Last Name: [Last], First Name: [First]"""

# Ask user for their fullname
fullname = input("What is your fullname: ").strip().title()

first_name, last_name = fullname.split(" ")

# Print splitted version into first name and last name
print(f"Last Name: {last_name}, First Name: {first_name}")