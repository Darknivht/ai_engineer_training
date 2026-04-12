"""Requirements:

Architecture: Use a main() function at the top. Call it at the very bottom. Do not write any executable logic in the global scope.
Modularity: You must define and use at least three custom helper functions:
clean_prompt(text): Takes a messy string, strips whitespace, capitalizes the first letter, and returns it.
calculate_api_cost(tokens): Takes an integer of tokens, calculates the cost (Assume the rate is $0.015 per 1,000 tokens), and returns the float cost.
generate_payload(system, user): Takes the two cleaned prompts, and uses an f-string and escape characters to return a single, beautifully formatted string block.
Execution in main():
Prompt the user for a System Prompt (Assume they type it messily).
Prompt the user for a User Prompt (Assume they type it messily).
Prompt the user for an Estimated Token Count (Assume they add accidental spaces. Strip it and cast it to an int).
Pass the data through your helper functions.
Final Output: Use a single print() statement in main() to output the final result. It must look exactly like this visually (including the lines, the quotes, the commas in the token count, and the exact USD formatting):
text

--- AI PAYLOAD PREPARED ---
System: "You are a helpful ai"
User: "Tell me a joke"
---------------------------
Tokens: 1,500
Estimated Cost: $0.0225"""

# Define a main func
def main():
    # Ask user for a system prompt
    sys_prompt = input("Enter System Prompt: ")
    # Prompt user for user prompt
    user_prompt = input("Enter User Prompt: ")
    # Prompt user for estimated token count strip and cast as int
    token_count = int(input("Enter Estimated Token Count: ").strip())
    # Pass data through helper funcs
    sys_prompt = clean_prompt(sys_prompt)
    user_prompt = clean_prompt(user_prompt)
    cost = calculate_api_cost(token_count)
    # Print out result
    print(f"{generate_payload(sys_prompt, user_prompt)}\nTokens: {token_count:,}\nEstimated Cost: ${cost:,.4f}")


# Define clean_prompt func with one param
def clean_prompt(text):
    # Clean user prompt and return it
    text = text.strip().capitalize()
    return text


# Define calculate_api_cost func with one param
def calculate_api_cost(token):
    # Calculate cost assuming rate is $0.015 per 1,000 tokens
    rate = 0.015
    div_token = token / 1000
    token = div_token * rate
    # Return as cost as a float
    return float(token)


# Define generate_payload with 2 params
def generate_payload(system, user):
    # Take the 2 cleaned user prompt and convert to beautifully formatted string block using f-string and escape characters and return
    return f"--- AI PAYLOAD PREPARED ---\nSystem: \"{system}\"\nUser: \"{user}\"\n---------------------------"


# Call main func
main()