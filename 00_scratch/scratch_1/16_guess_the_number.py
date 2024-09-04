# Guess the secret number (5 tries only)

import random
import sys

secret_number = random.randint(1, 20)

for i in range(1, 6):
    guess_number = input('Guess the secret number: ')
    guess_number = int(guess_number)
    if guess_number < secret_number:
        print('Your number is too low.')
    elif guess_number > secret_number:
        print('Your number is too high.')
    else:
        if guess_number == secret_number:
            print('You got it right in ' + str(i) + ' tries.')
            # break
            sys.exit()
        else:
            print('Invalid input.')
print('The secret number is: ' + str(secret_number))
