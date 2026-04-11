"""Task:
Define a function called get_token_count(). 
Inside it, ask the user for a token count, clean it, cast it to an integer, and return that integer. 
(Do not print it inside this function).
Define your main() function. 
Inside main(), call get_token_count(), save its returned value to a variable, and then print that variable.
Call main() at the bottom of the file."""

# Define get_token_count function
def get_token_count():
    # Ask user for token count within get_token_count function
    token_count = int("Enter Token Count: ").strip()
    return token_count

# Define main function
def main():
    # 
# Call get_token_count func inside main func
# Call main func