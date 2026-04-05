"""Task: Ask the user for a "System Prompt". 
The user will enter it messily (lots of spaces, all lowercase). 
You must clean it, put it inside double quotes, and append a specific hardcoded end-of-sequence token (e.g., <|endoftext|>) 
all on one line using an f-string and end="" behavior
"""

# Ask user for system prompt
system_prompt = input("Enter System Prompt For The AI: ")

# Clean user input
system_prompt = system_prompt.strip().capitalize()

# Print user input
print(f"\"{system_prompt}\"", end="")
print("<|endoftext|>")