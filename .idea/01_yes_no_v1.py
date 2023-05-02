"""MLG Yes / No
MLG stands for Maori Language Game.
Asks user if they have played this quiz before. The program only accepts yes or no as a answer which needs to be
changed in future components.
"""

# Ask the user if they have played before
show_instructions = input("have you played this quiz before?: ")

# If they say yes, output 'Program Continues'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'Display Instructions'
elif show_instructions == "no":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no")