import sys

while True:
    user_input = input('Type [exit] to end the program: ')
    if user_input == 'exit':
        sys.exit()
    print('You typed ' + user_input)