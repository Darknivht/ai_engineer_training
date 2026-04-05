"""The Context: You are using GPT-4o. You need to estimate the cost of a massive job.
Task: Prompt the user for "Total Tokens". Sanitize and cast to a float. Hardcode a variable price_per_token = 0.00002 (which is $0.02 per 1k tokens). Multiply them to get the total cost.
The Catch: You must print the final cost formatted as US Dollars with exactly two decimal places and commas using Python's f-string formatting trick (e.g., ${cost:,.2f}). Print: Estimated Cost: $[cost]"""

# Print Cost per 1k tokens
print("##############################\n# Cost per 1k tokens = $0.02 #\n##############################")

# Set price
price_per_token = 0.00002

# Ask user for Total Tokens and cast as float
total_tokens = float(input("Enter Total Tokens: ").strip())

# Calculate Estimated Cost
api_cost = total_tokens * price_per_token

# Print cost of api usage
print(f"Estimated Cost: {api_cost:.2f}")