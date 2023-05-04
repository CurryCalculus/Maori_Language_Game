"""Component 3 (Generate random quiz) v1
Generates random Maori numbers from 1-10 for users to translate in English.
This version will only work if the user says they want to do level 1."""

import random

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
    random_number = random.randint(1, 10)
    user_input = input(f"What is '{maori_numbers[random_number]}' in English?: ")

    if user_input == 'x':
        print("Good job! Come back again after some rest!")
        break

    correct_answer = str(random_number)

    if user_input == correct_answer:
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is '{correct_answer}'.")
