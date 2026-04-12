"""Task: Write a program called profile.py that:

Asks the user for their name, country, and favorite programming language (3 separate input() calls)
Stores each response in a descriptively-named variable (not x, y, z)
Prints a summary like:
text

Name: David
Country: Nigeria
Favorite Language: Python
Requirements:

Use comments above each logical section (gathering input, displaying output)
Use descriptive variable names
Run it 3 times with different inputs to verify it works"""

# Ask user for their name
name = input("What is your name?: ")
# Ask user for their country
country = input("What is your country?: ")
# Ask user for their favorite language
fav_lang = input("What is your favorite language?: ")

# Print out user inputs
print("Name:", name)
print("Country:", country)
print("Favorite Language:", fav_lang)