"""Component 5 (Score / Accuracy Tracker) v2
This version tells the user how many questions they have attempted, how many they got it right, and their accuracy
percentage
"""

import random

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

while True:
    # choose a random month
    month = random.choice(list(months_maori.keys()))

    # ask the user to translate the month
    user_input = input(f"What is the English name for '{months_maori[month]}'?: ")

    # check if the user wants to stop
    if user_input.lower() == "x":
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
    else:
        consecutive_correct_answers = 0
        total_questions_answered += 1
        print(f"Wrong. The correct answer is '{month}'.")


