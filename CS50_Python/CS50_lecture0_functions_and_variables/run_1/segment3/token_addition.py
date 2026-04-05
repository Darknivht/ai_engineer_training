"""Task: Prompt the user for "Input Tokens" and "Output Tokens". 
Using int(), cast them to integers. 
Add them together and print the total sum in an f-string (e.g., Total Tokens Used: [sum])"""

# Ask user for input and output tokens and cast them as int
input_tokens = int(input("Enter Total Input Tokens: "))
output_tokens = int(input("Enter Total Output Tokens: "))

# Add together the input and output tokens
total_tokens = input_tokens + output_tokens

# Print total sum using an f-string
print(f"Total Tokens Used: {total_tokens:,}")