"""Task:
Define a main() function.
Define a second function called greet_user(). Inside it, prompt the user for their name, sanitize it, and print a greeting.
Inside main(), call greet_user().
At the very bottom of your file (outside all indentation), call main().
"""
# Define main function
def main():
    greet_user()
# define greet_user function

def greet_user():
    # prompt user for their name and print 
    name = input("Enter your name: ").strip().title()
    print(f"Welcome {name}")
    
# Call main function
main()