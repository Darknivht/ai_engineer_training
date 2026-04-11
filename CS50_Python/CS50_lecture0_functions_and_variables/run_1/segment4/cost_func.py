"""Task:
Define main() at the top.
Define a helper function calculate_cost(tokens, rate). 
It must take exactly two parameters. Inside it, multiply them together and return the result.
Inside main(), ask the user for their "Token Count" (cast to int) and their "Cost per Token" (cast to float).
Pass both variables into calculate_cost().
Print the returned value in main(), formatted as US Dollars to 4 decimal places (e.g., $0.0450)."""

# Define main func
def main():
    # Ask user for Token count and cast as int
    token_count = int(input("Enter Token Count: ").strip())
    # Ask user for Cost Per Token and cast as float
    cost_per_token = float(input("Enter Cost Per Token: ").strip())
    # Pass both variables to calculate_cost() func
    cost = calculate_cost(token_count, cost_per_token)
    # Print returned value fomatted as US Dollar to 4 decimal places
    print(f"Your Cost is: ${cost:,.4f}")


# Define calculate_cost() func with tokens and rate as params
def calculate_cost(tokens, rate):
    # Inside claculate_cost() func multiply the 2 params and return value
    result = tokens * rate
    return result

# Call main func
main()