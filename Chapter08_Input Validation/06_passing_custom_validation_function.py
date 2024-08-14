import pyinputplus as pyip


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)  # Return an int form of numbers


response = pyip.inputCustom(addsUpToTen)  # No parenthesis after addsUpToTen
print(type(response))

# sample run:
# 123 -> The digits must add up to 10, not 6
# 12356 -> The digits must add up to 10, not 11
# 1234 -> 10 (VALID)