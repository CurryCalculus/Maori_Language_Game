"""Component 3 (Generate random quiz) v2
Generates the months of the year in Maori randomly.
This version will only work if the user chooses level 2."""

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
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is '{month}'.")





