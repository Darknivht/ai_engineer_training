"""Task: AI models use a "Temperature" setting (0.0 to 1.0) to control creativity. Write a function evaluate_temperature(temp) that takes a float parameter.
If temp is greater than 1.0, print Invalid: Temperature too high.
If temp is less than 0.0, print Invalid: Temperature too low.
Else, print Valid Temperature.
Call this function from main() after prompting the user for a float."""

# Define main func
def main():
    # Prompt user for temp and sanitise
    temp = float(input("Enter Temperture(0.0 - 1.0): ").strip())
    # Pass user input to evaluate_temperature(temp) func
    evaluate_temperature(temp)
    
# Define evaluate_temperature(temp) func
def evaluate_temperature(temp):
    # Check temp setting
    if temp > 1.0:
        print("Invalid: Temperature too high")
    elif temp < 0.0:
        print("Invalid: Temperature too low")
    else:
        print("Valid Temperature")
        
# Call main func
main()