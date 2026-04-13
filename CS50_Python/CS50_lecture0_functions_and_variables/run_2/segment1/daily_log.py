"""Task: Write daily_log.py — a simple daily log entry generator:

Ask the user for: today's date, what they learned, what they struggled with, and tomorrow's goal
Store each in a variable
Print a formatted log entry:
===== DAILY LEARNING LOG =====
Date: 2024-01-15
Learned: How to use variables in Python
Struggled with: Understanding return values
Tomorrow's goal: Build a calculator program
==============================
"""
# Ask user for today's date, what they learned, what they struggled with, and tomorrow's goal
todays_date = input("What is today's date?: ").strip()
user_learned = input("What did you learn today?: ").strip()
struggled_with = input("What did you struggle with?: ").strip()
tomorrows_goal = input("What is your goal for tomorrow?: ").strip()
seperator = "="

# Print a formatted log entry
print(f"""{seperator * 4} DAILY LEARNING LOG {seperator * 4}
Date: {todays_date}
Learned: {user_learned}
Struggled with: {struggled_with}
Tomorrow's goal: {tomorrows_goal}
{seperator * 20}""")