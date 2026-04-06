"""Task Requirements:

Prompt the user for "Total Tokens Used".
The user will type something horribly messy, like: " 50000 " (with tons of spaces).
Sanitize the string (strip it).
Cast it to a float type.
Divide it by 1000.
Multiply that result by 0.03 (representing $0.03 per 1k tokens).
Store the final result in a variable called final_cost.
Print the exact output: Final Price: $[final_cost] formatted to exactly three decimal places with commas (e.g., if the cost is 1500, it should print $1,500.000)"""


# Print token price
print("##############################\n# Cost per 1k tokens = $0.03 #\n##############################")
token_price = 0.03

# Ask user for total tokens used clean and cast to float
total_tokens_used = float(input("Enter Total Tokens Used: ").strip())
# Divide total_tokens_used by 1000
tokens_divided = total_tokens_used / 1000

# Multiply by 0.03 price of 1k tokens
final_cost = tokens_divided * token_price

# print final_cost
print(f"Final Price is: ${final_cost:,.3f}")