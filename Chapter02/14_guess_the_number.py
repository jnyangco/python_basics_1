import random

secret_number = random.randint(1, 20)
print('Computer: I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times only
for guess_counter in range(1, 7): #start 1 to 6 tries only
    print('Take a guess.')
    guess_number = int(input())
    if guess_number < secret_number:
        print('Your guess is too low.')
    elif guess_number > secret_number:
        print('Your guess is too high.')
    else:
        print('Good job! You guessed my number in ' + str(guess_counter) + ' tries.')
        break

if guess_number == secret_number:
    print('Good job! You guessed my number in ' + str(guess_counter) + ' tries.')
else:
    print('Nope. The number I was thinking of was ' + str(secret_number))