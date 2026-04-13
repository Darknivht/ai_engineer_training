"""Task: Write interview_prep.py — a program that simulates a mini job interview preparation tool:

Ask the user for: their name, the company they're applying to, the role they want, and one skill they're strongest in
Print a formatted elevator pitch like:
--- Your Elevator Pitch ---
Hi, my name is David. I'm excited to apply for the AI Engineer role at Google. My strongest skill is machine learning, and I believe it makes me a great fit for this position.
Requirements:

Use pseudocode comments FIRST, then implement
The output must read like natural English (watch your spacing and punctuation)
Use at least 4 variables with descriptive names"""

# Ask user for their name, company they're applying to, role they want, and one skill they are stringest in
name = input("What is your name?: ").strip().title()
company = input("What company are you applying to?: ").strip().title()
role = input("What role do you want?: ").strip().title()
skill = input("What is your strongest skill?: ").strip().title()

# Print out a fomratted elevated pitch
print(f"--- Your Elevator Pitch ---\nHi, my name is {name}. I'm excited to apply for the {role} role at {company}. My strongest skill is {skill}, and I believe it makes me a great fit for this position.")