"""Component 5 (Score / Accuracy Tracker) v1
This version tells the user how many questions they have attempted, how many they got it right, and their accuracy
percentage
"""

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
num_questions_attempted = 0
num_correct_answers = 0

while True:
    random_number = random.randint(1, 10)
    user_input = input(f"What is '{maori_numbers[random_number]}' in English?: ")

    if user_input == 'x':
        print("Good job! Come back again after some rest!")
        break

    num_questions_attempted += 1
    correct_answer = str(random_number)

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
