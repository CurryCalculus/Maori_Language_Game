"""Component 4 (Answer Validation / Feedback) v2
This component builds on from component 3.
The user will receive a compliment if they get 10 questions right in row and the quiz will suggest you go back a level
if you get more than 20 questions.
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

while True:
    # choose a random quiz type (months or numbers)
    quiz_type = random.choice(['months', 'numbers'])

    if num_wrong > 20:
        print(
            "You've answered more than 20 questions wrong. Let's go back to level 1 if you struggle with numbers and level 2 if you struggle with months.")
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
            print("Good job! Come back again after some rest!")
            break

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
            print("Good job! Come back again after some rest!")
            break

        correct_answer = str(random_number)

        # check if the user's answer is correct
        if user_input == correct_answer:
            num_correct += 1
            consecutive_correct += 1
            print("Correct!")
        else:
            consecutive_correct = 0
            num_wrong += 1
            print("Wrong! Try again later :)")

    # check if the user has answered 10 questions correctly in a row
    if consecutive_correct == 10:
        print("Well done! Keep up the hard work!")


