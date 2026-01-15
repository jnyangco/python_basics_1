def comma_code(list_values):
    for i in range(len(list_values)):
        if i < (len(list_values) - 1):
            print(list_values[i], end=', ')
        else:
            # print('and ' + list_values[i]) # this will fail if last item in the list is not a string
            print(f'and {list_values[i]}')


spam = ['apples', 'bananas', 'tofu', 'cats', 'hello', 2, 4]
comma_code(spam)

