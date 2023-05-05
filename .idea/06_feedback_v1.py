"""Component 4 (Answer Validation / Feedback) v1
This component builds on from component 3.
The user will receive a compliment if they get 10 questions right in row."""

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

consecutive_correct_answers = 0

while True:
    random_number = random.randint(1, 10)
    user_input = input(f"What is '{maori_numbers[random_number]}' in English?: ")

    if user_input == 'x':
        print("Good job! Come back again after some rest!")
        break

    correct_answer = str(random_number)

    if user_input == correct_answer:
        consecutive_correct_answers += 1
        if consecutive_correct_answers == 10:
            print("Well done! Keep up the hard work!")
        else:
            print("Correct!")
    else:
        consecutive_correct_answers = 0
        print(f"Wrong. The correct answer is '{correct_answer}'.")









