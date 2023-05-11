"""MLG component v4
Making few changes from v3
"""
import random


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
    print()
    print(formatter("*", "how to Play"))
    print()
    print("This quiz is designed for students who want to"
          "\nbecome fluent in translating Maori numbers from"
          "\n1-10 and the months of the year to English.")
    print()
    print("1. Choose what level you want to do:"
          "\n Level 1 = numbers"
          "\n Level 2 = months of the year"
          "\n Level 3 = mixture of both")
    print()
    print("2. Answer the questions. The quiz will run infinitely until you say 'x'."
          "\n When you say 'x' the quiz will stop and you will know how many questions"
          "\n you've attempted, how many you got it correct, and your accuracy percentage.")
    print()
    print("<Quick Notes>")
    print()
    print("1. If you say 'x' or any alphabet as your first answer you will be told to enter an integer."
          "\n2. You will only know the correct answer for level 1 and 2. Level 3 is strict with the marking so please be careful.")
    print()
    print("Enjoy the quiz and I hope you become more familiar with Maori numbers and months :) ")
    print("*" * 50)
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

# Function for level 1
def maori_numbers_quiz():
    maori_numbers = {
        1: 'tahi',
        2: 'rua',
        3: 'toru',
        4: 'wha',
        5: 'rima',
        6: 'ono',
        7: 'whitu',
        8: 'waru',
        9: 'iwa',
        10: 'tekau'
    }

    consecutive_correct_answers = 0
    num_questions_attempted = 0
    num_correct_answers = 0
    has_attempted_question = False

    while True:
        random_number = random.randint(1, 10)
        correct_answer = str(random_number)
        user_input = input(f"What is '{maori_numbers[random_number]}' in English?: ")

        if user_input.lower() == 'x':
            if has_attempted_question:
                print("Good job! Come back again after some rest!")
                break
            else:
                print("You haven't attempted any questions yet. Please try answering a question first.")
        else:
            has_attempted_question = True
            num_questions_attempted += 1

            if user_input == correct_answer:
                consecutive_correct_answers += 1
                num_correct_answers += 1
                if consecutive_correct_answers == 10:
                    print("Well done! Keep up the hard work!")
                else:
                    print("Correct!")
            else:
                consecutive_correct_answers = 0
                print(f"Wrong. The correct answer is '{correct_answer}'.")

    accuracy_percentage = round(num_correct_answers/num_questions_attempted * 100, 2)
    print(f"You attempted a total of {num_questions_attempted} questions.")
    print(f"You got {num_correct_answers} questions correct before pressing 'x'.")
    print(f"Your accuracy percentage is {accuracy_percentage}%.")


# Function for level 2
def maori_to_english():
    months_maori = {
        "January": "Kohi-tatea",
        "February": "Hui-tanguru",
        "March": "Poutu-te-rangi",
        "April": "Paenga-whawha",
        "May": "Haratua",
        "June": "Pipiri",
        "July": "Hongongoi",
        "August": "Here-turi-koka",
        "September": "Mahuru",
        "October": "Whiringa-a-nuku",
        "November": "Whiringa-a-rangi",
        "December": "Hakihea",
    }

    consecutive_correct_answers = 0
    total_questions_answered = 0
    total_correct_answers = 0
    first_attempt = True

    while True:
        # choose a random month
        month = random.choice(list(months_maori.keys()))

        # ask the user to translate the month
        user_input = input(f"What is the English name for '{months_maori[month]}'?: ")

        # check if the user wants to stop
        if total_questions_answered != 0 and user_input.lower() == "x":
            accuracy_percentage = (total_correct_answers / total_questions_answered) * 100
            print(f"You attempted a total of {total_questions_answered} questions. "
                  f"\nYou got {total_correct_answers} questions correct before pressing 'x'. "
                  f"\nYour accuracy percentage is {accuracy_percentage}%.")
            break

        # check if the user's answer is correct
        if user_input.lower() == month.lower():
            consecutive_correct_answers += 1
            total_correct_answers += 1
            total_questions_answered += 1
            if consecutive_correct_answers == 10:
                print("Well done! Keep up the hard work!")
            else:
                print("Correct!")
            first_attempt = False
        else:
            consecutive_correct_answers = 0
            total_questions_answered += 1
            if first_attempt == 'x':
                print("You haven’t attempted any questions yet. Please try answering a question first.")
                first_attempt = False
            else:
                print(f"Wrong. The correct answer is '{month}'.")


# Function for level 3
def maori_quiz():
    months_maori = {
        "January": "Kohi-tatea",
        "February": "Hui-tanguru",
        "March": "Poutu-te-rangi",
        "April": "Paenga-whawha",
        "May": "Haratua",
        "June": "Pipiri",
        "July": "Hongongoi",
        "August": "Here-turi-koka",
        "September": "Mahuru",
        "October": "Whiringa-a-nuku",
        "November": "Whiringa-a-rangi",
        "December": "Hakihea",
    }

    maori_numbers = {
        1: 'tahi',
        2: 'rua',
        3: 'toru',
        4: 'wha',
        5: 'rima',
        6: 'ono',
        7: 'whitu',
        8: 'waru',
        9: 'iwa',
        10: 'tekau'
    }

    # set up variables to track correct answers and consecutive correct answers
    num_correct = 0
    consecutive_correct = 0
    num_wrong = 0
    num_attempted = 0

    while True:
        # choose a random quiz type (months or numbers)
        quiz_type = random.choice(['months', 'numbers'])

        if num_wrong > 20:
            print("You've answered more than 20 questions wrong. Let's go back to level 1 if you struggle with numbers and level 2 if you struggle with months.")
            if quiz_type == 'months':
                quiz_type = 'numbers'
            else:
                quiz_type = 'months'
            num_wrong = 0

        if quiz_type == 'months':
            # choose a random month
            month = random.choice(list(months_maori.keys()))

            # ask the user to translate the month
            user_input = input(f"What is the English name for '{months_maori[month]}'?: ")

            # check if the user wants to stop
            if user_input.lower() == "x":
                accuracy_percentage = (num_correct/num_attempted) * 100 if num_attempted > 0 else 0
                print(f"You attempted a total of {num_attempted} questions.\nYou got {num_correct} correct before pressing 'x'.\nYour accuracy percentage is {accuracy_percentage:.2f}%.")
                return

            num_attempted += 1

            # check if the user's answer is correct
            if user_input.lower() == month.lower():
                num_correct += 1
                consecutive_correct += 1
                print("Correct!")
            else:
                consecutive_correct = 0
                num_wrong += 1
                print("Wrong! Try again later :)")

        else:
            # choose a random number
            random_number = random.randint(1, 10)
            user_input = input(f"What is '{maori_numbers[random_number]}' in English?: ")

            # check if the user wants to stop
            if user_input == 'x':
                accuracy_percentage = (num_correct/num_attempted) * 100 if num_attempted > 0 else 0
                print(f"You attempted a total of {num_attempted} questions.\nYou got {num_correct} correct before pressing 'x'.\nYour accuracy percentage is {accuracy_percentage:.2f}%.")
                return

            num_attempted += 1

            correct_answer = str(random_number)

            # check if the user's answer
            if user_input.lower() == correct_answer:
                num_correct += 1
                consecutive_correct += 1
                print("Correct!")
            else:
                consecutive_correct = 0
                num_wrong += 1
                print("Wrong! Try again later :)")


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
print(formatter("-", "Maori Language Game"))
print()
played_before = yes_no("Have you played this quiz before? ")

if played_before == "No":
    instructions()

# Call the function to get the quiz difficulty level and store the result in a variable
difficulty_level = get_quiz_difficulty()

# Print a message indicating the user's chosen difficulty level
print("You chose", difficulty_level, "difficulty.")

if difficulty_level == "easy":
    maori_numbers_quiz()
elif difficulty_level == "medium":
    maori_to_english()
else:
    maori_quiz()

print(formatter("*", "Good job for completing today’s session! Do this daily and your Māori will improve!"))


#
# # Function that runs level 1
# maori_numbers_quiz()
#
# # Function that runs level 2
# if __name__ == '__main__':
#     maori_to_english()
#
# # Function that runs level 3
# maori_quiz()
