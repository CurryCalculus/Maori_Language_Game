"""Component 7 (Statement formatter) v1
Making the quiz more aesthetic"""

symbol = "*"
text = "hello world"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)