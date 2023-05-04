"""Component 2 (Difficulty) v4
Changing v2 into a function. Changing it to a function can help improve code quality, reusability, maintainability, and
readability. It also helps to reduce code complexity and improve testing and debugging."""


# Define a function to get the quiz difficulty level from the user
def get_quiz_difficulty():
    # Prompt user to choose quiz difficulty level
    difficulty = input("How difficult do you want the quiz to be? "
                       "\n(1 = easy, 2 = medium, 3 = hard): ")

    # Loop until user enters a valid input
    while True:
        # Check user's input and return appropriate message
        if difficulty == "1":
            return "easy"
        elif difficulty == "2":
            return "medium"
        elif difficulty == "3":
            return "hard"
        else:
            # Prompt user to choose quiz difficulty level again
            difficulty = input("Invalid input. "
                               "\nPlease choose a whole number between 1-3: ")

# Main routine
# Call the function to get the quiz difficulty level and store the result in a variable
difficulty_level = get_quiz_difficulty()

# Print a message indicating the user's chosen difficulty level
print("You chose", difficulty_level, "difficulty.")

