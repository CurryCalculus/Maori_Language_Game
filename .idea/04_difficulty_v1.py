"""Ask the user how difficult they want the quiz to be. The user has 3 options (1 being easy, 2 being medium, and
3 being hard). This version will ask the question and tell them what difficulty they are going to do."""

# Prompt user to choose quiz difficulty level
difficulty = input("Choose quiz difficulty (1 = easy, 2 = medium, 3 = hard): ")

# Check user's input and print appropriate message
if difficulty == "1":
    print("You chose easy difficulty.")
elif difficulty == "2":
    print("You chose medium difficulty.")
elif difficulty == "3":
    print("You chose hard difficulty.")
else:
    print("Invalid input. Please choose a whole number between 1-3: ")
