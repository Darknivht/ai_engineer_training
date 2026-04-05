"""The Bug Hunter: Deliberately introduces syntax errors and bugs into a script. The student must read the CLI
error messages, identify the errors, and fix them. Builds essential debugging skills.
"""
# -------- TERMINAL ERROR 1 -------
"""Could not find platform independent libraries <prefix>
  File "c:\Users\Toshiba\Desktop\ai_engineer_training\CS50_Python\CS50_lecture0_functions_and_variables\segment1\bug_hunter.py", line 13
    name = input("What is your name: ).strip().title()
                 ^
SyntaxError: unterminated string literal (detected at line 13)"""

# ------ SOLUTION ------
"""Closed the string in the name input function"""

# -------- TERMINAL ERROR 2 -------
"""Could not find platform independent libraries <prefix>
  File "c:\Users\Toshiba\Desktop\\ai_engineer_training\CS50_Python\CS50_lecture0_functions_and_variables\segment1\bug_hunter.py", line 16
    college = input"What college are you attending: ").strip().title()
                                                     ^
SyntaxError: unmatched ')'"""

# ------ SOLUTION ------
"""Added the opening bracket in the input function of college variable"""

# -------- TERMINAL ERROR 1 -------
# Could not find platform independent libraries <prefix>
#   File "c:\Users\Toshiba\Desktop\ai_engineer_training\CS50_Python\CS50_lecture0_functions_and_variables\segment1\bug_hunter.py", line 5
    # """Could not find platform independent libraries <prefix>
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 65-66: truncated \UXXXXXXXX escape

# ------ SOLUTION ------
"""Fixed the college variable in print function"""


name = input("What is your name: ").strip().title()
college = input("What college are you attending: ").strip().title()

print(f"Hey, {name} you attend {college}")
