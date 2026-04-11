"""Task:
Define main() at the top.
Define a helper function clean_text(text) that takes exactly one parameter (text). 
Inside it, strip the text, title-case it, and return it.
Inside main(), ask the user for a "System Role" (e.g., " helpful AI assistant ").
Still inside main(), pass that input into clean_text(), save the returned value, and print it using an f-string: Cleaned Role: [Result]."""

# Define main func
def main():
    # Ask user for system role
    system_role = input("Enter System Role: ")
    # Pass system role to the cleaner func
    cleaned_role = clean_text(system_role)
    print(f"Cleaned Role: {cleaned_role}")

# Define clean_text func with one param
def clean_text(text):
    # Clean text and return it
    text = text.strip().title()
    return text

# Call main func
main()