
spam = 1

if spam == 0:
    print('Hello')
elif spam == 1:
    print('Howdy')
else:
    print('Greetings!')


i = 1
while True:
    print('Guess the number: ')
    user_input = input()
    if int(user_input) == 10:
        break

    # print(i)
    # if i == 10:
    #     break
    # i = i + 1