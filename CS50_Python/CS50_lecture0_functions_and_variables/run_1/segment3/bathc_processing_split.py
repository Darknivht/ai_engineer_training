"""The Context: You have 10,000 documents to embed into a vector database, but the API only accepts batches of 250.
Task: Prompt the user for "Total Documents" and "Batch Size". 
Sanitize, then cast them to integers. Calculate how many batches it will take using division (/). 
Because standard division returns a float (e.g., 40.0), use int() to cast the final answer back to a clean integer (e.g., 40). 
Print: You will need [batches] batches"""

# Ask user for total documents and batch size and cast to int
total_docs = int(input("Enter Total Documents: ").strip())
batch_size = int(input("Enter Batch Size: ").strip())

# Calculate batches
batches = int(total_docs / batch_size)

# Print number of batches
print(f"You will need {batches} batches")