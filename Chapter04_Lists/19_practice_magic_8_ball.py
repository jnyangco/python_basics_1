import random


messages_list = ['#1 It is certain', '#2 Yes', '#3 No', '#4 Maybe', '#5 Please try again']

# 1. random.choice
# print(random.choice(messages_list))

# 2. random.randint(from index, to index)
print(messages_list[random.randint(0, len(messages_list) - 1)])


