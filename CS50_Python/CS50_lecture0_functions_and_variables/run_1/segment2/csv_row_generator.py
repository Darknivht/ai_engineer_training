"""Task: Prompt the user for three separate words using three separate input() calls (e.g., "Apple", "Banana", "Cherry"). Print them out on a single line separated by commas, without using an f-string or concatenation (+). (Hint: use the sep parameter inside the print() function)"""

# Ask user for 3 word inputs
word1 = input("Enter a random word: ").strip().title()
word2 = input("Enter another random word: ").strip().title()
word3 = input("Enter another random word: ").strip().title()

# Print words on a single line "," separated not f-string or concatenation
print(word1, word2, word3, sep=", ")
