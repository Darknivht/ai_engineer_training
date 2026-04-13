"""Task: Write formatter.py that:

Asks the user for their first name, last name, and city
Prints the SAME greeting in 3 different ways:
Using string concatenation (+)
Using multiple arguments to print() with commas
Using an f-string"""

# Asks the user for their first name, last name, and city
first_name = input("Enter first name: ").strip().capitalize()
last_name = input("Enter last name: ").strip().capitalize()
city = input("Enter City: ").strip().capitalize()

# Print greeting using concatenation
print("Hello, " + first_name + " " + last_name + " from " + city + "!")
# Print greeting using multiple args comma separated
print("Hello, ",first_name," ",last_name," from ",city,"!", sep="")
# Print greeting using f-string
print(f"Hello, {first_name} {last_name} from {city}!")


# I 100% prefer f-string its way easier to use and much more convenient