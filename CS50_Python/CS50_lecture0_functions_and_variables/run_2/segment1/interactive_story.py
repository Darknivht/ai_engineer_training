"""Write story.py — an interactive story generator that goes beyond what was explicitly taught:

The program asks the user at least 6 questions to gather story elements (character name, location, object, emotion, action, number)
Using those inputs, construct and print a coherent 5-sentence story that uses ALL of the user's inputs
The story should make grammatical sense regardless of what the user types
Example output:

Once upon a time, David traveled to Lagos carrying a mysterious laptop.
Feeling excited, David decided to code for 7 hours straight.
..."""

# Ask user questions for the story
character_name = input("What is your character's name: ").strip().capitalize()
location = input("What is the location: ").strip().capitalize()
verb1 = input("Enter a random verb: ").strip()
verb2 = input("Enter another random verb: ").strip()
noun1 = input("Enter a random noun: ").strip().capitalize()
noun2 = input("Enter another random noun: ").strip().capitalize()

# Print out the story
print(f"""{"=" * 6} Generated Story {"=" * 6}
Once upon a time, in {location},
There lived {character_name},
{character_name} likes {verb1} every morning.
One day while {character_name} was {verb1}, {character_name} remembered {noun1}.
{noun2} was {character_name}'s favorite.
{character_name} is tired whenever they {verb2}.
{noun2} is a beautiful thing that {character_name} loves""")
