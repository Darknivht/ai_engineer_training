"""Task: Build a script with a main() function. Prompt the user for a "Task Type" and sanitize it to lowercase.
If they type "image" or "vision", print Routing to: DALL-E 3.
If they type "audio" or "voice", print Routing to: Whisper.
If they type "text", print Routing to: GPT-4o.
For anything else, print Error: Unknown task type.
"""

# Define main func
def main():
    # Task Types
    print("TASK TYPES")
    print(f"{"#" * 35}\nImage, Vision, Audio, Voice or Text\n{"#" * 35}")
    # Prompt user for task type and sanitise
    task_type = input("Enter Task Type: ").strip().lower()
    # Pass user input to router func
    router(task_type)

# Define router func
def router(task_type):
    # Check task type
    if task_type == "image" or task_type == "vision":
        print("Routing to: DALL-E 3.")
    elif task_type == "audio" or task_type == "voice":
        print("Routing to: Whisper.")
    elif task_type == "text":
        print("Routing to: GPT-4o.")
    else:
        print("Error: Unknown task type.")

# call main func
main()