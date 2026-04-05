# Task: Write a program that prompts the user for their name and their favorite AI tool (e.g., ChatGPT, Claude), then prints a concatenated greeting.

# Ask user for their name
name = input("What is your name: ").strip().title()

# Ask user their favorite AI tool
fav_tool = input("What is your favorite AI tool: ").strip()

# Print concatenated greeting
print("Hello, " + name + " your favorite AI tool is " + fav_tool)