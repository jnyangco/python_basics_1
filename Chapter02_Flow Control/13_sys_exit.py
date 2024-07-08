import sys

while True:
    print('Type [exit] to end the program.')
    response = input()
    if response == 'exit':
        print('Program Exit!')
        sys.exit()
    print('You typed ' + response + '.')