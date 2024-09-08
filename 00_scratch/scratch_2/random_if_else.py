

import random


def answer(number):
    if number == 1:
        return "Yes"
    elif number == 2:
        return "No"
    elif number == 3:
        return "Maybe"


number1 = random.randint(1, 3)
print(answer(number1))

