"""Component 4 (Answer Validation / Feedback) v2
This component builds on from component 3.
The user will receive a compliment if they get 10 questions right in row."""

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

while True:
    # choose a random month
    month = random.choice(list(months_maori.keys()))

    # ask the user to translate the month
    user_input = input(f"What is the English name for '{months_maori[month]}'?: ")

    # check if the user wants to stop
    if user_input.lower() == "x":
        print("Good job! Come back again after some rest!")
        break

    # check if the user's answer is correct
    if user_input.lower() == month.lower():
        consecutive_correct_answers += 1
        if consecutive_correct_answers == 10:
            print("Well done! Keep up the hard work!")
        else:
            print("Correct!")
    else:
        consecutive_correct_answers = 0
        print(f"Wrong. The correct answer is '{month}'.")







