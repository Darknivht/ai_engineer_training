"""Task: AI classification models return probabilities (e.g., 0.857392). 
Prompt the user for a "Model Confidence Score".
Cast it to a float. Use the round() function to round it to exactly two decimal places. 
Print the result: Final Confidence: [score]"""

# Ask user for model confidence score
model_confidence_score = input("Enter Model Confidence Score: ").strip()

# Cast to float and round to 2 decimal places
model_confidence_score = round(float(model_confidence_score), 2)

# print result
print(f"Final Confidence: {model_confidence_score}")