"""Updated version of 04_difficulty_v1
The code is now a loop so even if the user put a code that's invalid they don't need to run the code again. """

# Prompt user to choose quiz difficulty level
difficulty = input("How difficult do you want the quiz to be (1 = easy, 2 = medium, 3 = hard): ")

# Loop until user enters a valid input
while True:
    # Check user's input and print appropriate message
    if difficulty == "1":
        print("You chose easy difficulty.")
        break
    elif difficulty == "2":
        print("You chose medium difficulty.")
        break
    elif difficulty == "3":
        print("You chose hard difficulty.")
        break
    else:
        # Prompt user to choose quiz difficulty level again
        difficulty = input("Invalid input. Please choose a whole number between 1-3: ")

