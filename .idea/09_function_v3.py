"""Componet 7 (Game Mechanics / Looping) v3
I changed my level 1 code to a function to assemble it to my MLG base component.
"""

import random

def maori_quiz():
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
    num_attempted = 0

    while True:
        # choose a random quiz type (months or numbers)
        quiz_type = random.choice(['months', 'numbers'])

        if num_wrong > 20:
            print("You've answered more than 20 questions wrong. Let's go back to level 1 if you struggle with numbers and level 2 if you struggle with months.")
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
                accuracy_percentage = (num_correct/num_attempted) * 100 if num_attempted > 0 else 0
                print(f"You attempted a total of {num_attempted} questions.\nYou got {num_correct} correct before pressing 'x'.\nYour accuracy percentage is {accuracy_percentage:.2f}%.")
                return

            num_attempted += 1

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
                accuracy_percentage = (num_correct/num_attempted) * 100 if num_attempted > 0 else 0
                print(f"You attempted a total of {num_attempted} questions.\nYou got {num_correct} correct before pressing 'x'.\nYour accuracy percentage is {accuracy_percentage:.2f}%.")
                return

            num_attempted += 1

            correct_answer = str(random_number)

            # check if the user's answer
            if user_input.lower() == correct_answer:
                num_correct += 1
                consecutive_correct += 1
                print("Correct!")
            else:
                consecutive_correct = 0
                num_wrong += 1
                print("Wrong! Try again later :)")

            # check if the user has answered 3 consecutive questions correctly
        if consecutive_correct == 3:
            consecutive_correct = 0
            print("Congratulations! You've answered 3 consecutive questions correctly. You're now at the next level!")
            if quiz_type == 'months':
                # move to the next level of months quiz
                months_maori.pop(month)
                if len(months_maori) == 0:
                    print("You've learned all the months in Maori!")
                    break
            else:
                # move to the next level of numbers quiz
                maori_numbers.pop(random_number)
                if len(maori_numbers) == 0:
                    print("You've learned all the numbers in Maori!")
                    break

        # print final results
        accuracy_percentage = (num_correct / num_attempted) * 100 if num_attempted > 0 else 0
        print(
            f"You attempted a total of {num_attempted} questions.\nYou got {num_correct} correct.\nYour accuracy percentage is {accuracy_percentage:.2f}%.")

# call the maori_quiz function
maori_quiz()




