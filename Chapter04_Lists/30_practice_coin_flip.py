import random

i = 0
number_of_streaks = 0
for experiment_number in range(10000):

    list_head_tails = []
    print('#' + str(experiment_number + 1), end=' -> ')
    for i in range(100):
        random_num = random.randint(0, 1)

        if random_num == 0:
            print('H', end=' ')
            list_head_tails.append('H')
        else:
            print('T', end=' ')
            list_head_tails.append('T')
    print('')
    # print(list_head_tails)

    head_streaks = 0
    tail_streaks = 0
    for i in range(len(list_head_tails)):
        if list_head_tails[i] == 'H':
            head_streaks = head_streaks + 1
            tail_streaks = 0
            if head_streaks == 6:
                number_of_streaks = number_of_streaks + 1
                head_streaks = 0
                # print(str(number_of_streaks) + ' H H H H H H')
        else:
            tail_streaks = tail_streaks + 1
            head_streaks = 0
            if tail_streaks == 6:
                number_of_streaks = number_of_streaks + 1
                tail_streaks = 0
                # print(str(number_of_streaks) + ' T T T T T T')

print('\n Number of streaks ---> ' + str(number_of_streaks))



