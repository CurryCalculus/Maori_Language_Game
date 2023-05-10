"""Componet 7 (Game Mechanics / Looping) v2
I changed my level 1 code to a function to assemble it to my MLG base component.
"""

import random

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
            if first_attempt:
                print("You haven’t attempted any questions yet. Please try answering a question first.")
                first_attempt = False
            else:
                print(f"Wrong. The correct answer is '{month}'.")

if __name__ == '__main__':
    maori_to_english()

