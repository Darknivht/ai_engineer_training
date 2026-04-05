"""Task: Ask the user for an "Instruction" and a "Topic". You must print a formatted AI prompt using a single print() statement. Use escape characters (\n for new lines and \" for quotes) to make the terminal output"""

# Ask User for an Instruction
instruction = input("Provide instruction to the AI: ").strip().capitalize()

# Ask User for a Topic
topic = input("Provide topic to the AI: ").strip().capitalize()

# Print a formatted AI prompt using a single print() statement
print(f"System: \"You are an AI\"\nInstruction:\n{instruction} -> {topic}")