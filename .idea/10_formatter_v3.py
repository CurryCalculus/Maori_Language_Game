"""Component 7 (Statement formatter) v2
Call the function 2 times - once for each of the tests
"""


# Function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# main routine
print(formatter("-", "Maori Language Game"))
print()
print(formatter("*", "Good job for completing today’s session! Do this daily and your Māori will improve!"))


