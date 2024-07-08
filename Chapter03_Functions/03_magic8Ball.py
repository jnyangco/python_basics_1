import random


def get_answer(answer_number):
    if answer_number == 1:
        return '#1 It is certain'
    elif answer_number == 2:
        return '#2 Yes'
    elif answer_number == 3:
        return '#3 No'
    elif answer_number == 4:
        return '#4 Maybe'
    elif answer_number == 5:
        return '#5 Please try again'


r = random.randint(1, 5)
answer = get_answer(r)
print(answer)


# Short version of the code above
# print(get_answer(random.randint(1, 5)))

