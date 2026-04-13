"""Task: Write email_gen.py that:

Asks the user for their full name (e.g., " John DOE ")
Asks for their company name (e.g., " GOOGLE ")
Cleans both inputs (strip whitespace, fix capitalization)
Generates a professional email address in lowercase: john.doe@google.com
Prints both the clean name and the generated email
Expected output:

Clean Name: John Doe
Email: john.doe@google.com
Requirements:

Handle messy input gracefully
You'll need to figure out how to make strings lowercase (hint: there's a method called .lower() — look it up in Python's string documentation!)
You'll need to use .replace() to swap the space between first and last name with a dot (look this up too!)
Use f-strings for the final output"""

# Ask user for full name
full_name = input("What is your full name?: ").strip().title()

# Ask user for company name
company = input("What company do you work for: ").strip().title()
# Generate email
dotted_name = full_name.replace(" ", ".").lower()
mail = (f"{dotted_name}@{company.lower()}.com")
# Print user full name and mail
print(f"Clean Name: {full_name}\nEmail: {mail}")