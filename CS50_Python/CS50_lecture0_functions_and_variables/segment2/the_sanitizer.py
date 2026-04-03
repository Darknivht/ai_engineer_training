"""Task: Prompt the user for their name, expecting them to add messy spaces and weird capitalization (e.g., " dAvId "). Use chained methods to clean it and print the perfect version using an f-string"""

# Ask user for their name
name = input("Enter your name: ").strip().title()

# Print cleaned up user name using f string
print(f"Name: {name}")