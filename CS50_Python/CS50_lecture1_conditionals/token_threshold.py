"""Task: Write a program that prompts the user for their "Prompt Token Count" (cast to int). 
If the count is greater than 128000, print Context Window Exceeded.. 
Otherwise, print Prompt Accepted."""

# Define main func
def main():
    # Prompt user for prompt token count and sanitise
    prompt_token_count = int(input("Enter Prompt Token Count: ").strip())
    context_window_checker(prompt_token_count)

# Define context_window_checker func
def context_window_checker(prompt_token_count):
    # Set context_window
    context_window = 128000
    # Check whether token count fits context window
    if prompt_token_count > context_window:
        print("Context Window Exceeded..")
    else:
        print("Prompt Accepted.")
        
        
main()