"""Component 3 (Generate random quiz) v2
Generates random Maori numbers from 1-10 and the months of year in Maori. The code will no longer tell you the
correct answers. This version only works if the user chooses level 3."""

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

while True:
    # choose a random quiz type (months or numbers)
    quiz_type = random.choice(['months', 'numbers'])

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
            print("Correct!")
        else:
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
            print("Correct!")
        else:
            print("Wrong! Try again later :)")







