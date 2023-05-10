"""Componet 7 (Game Mechanics / Looping) v1
I changed my level 1 code to a function to assemble it to my MLG base component.
"""

import random

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

maori_numbers_quiz()  # Call the function to run it.
