"""MLG component
Components added after they have been created and tested"""


# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'Display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no")


# function to display instructions
def instructions():
    print("***** How to Play *****")
    print()
    print("The rules of the game will go here")
    print()



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


# Main Routine go here...
played_before = yes_no("Have you played this quiz before? ")

if played_before == "No":
    instructions()


# Call the function to get the quiz difficulty level and store the result in a variable
difficulty_level = get_quiz_difficulty()

# Print a message indicating the user's chosen difficulty level
print("You chose", difficulty_level, "difficulty.")