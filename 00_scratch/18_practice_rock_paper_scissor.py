import random
import sys

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True:
        print('Enter your move: R, P, S, Q')
        user_move = input()
        if user_move == 'r' or user_move == 'p' or user_move == 's':
            break
        elif user_move == 'q':
            sys.exit()
        else:
            print('Invalid input.')
            continue

    computer_move_list = ['r', 'p', 's']
    computer_move = random.choice(computer_move_list)
    # print('Computer Move is ' + computer_move)

    print(f'User({user_move}) VS. Computer({computer_move})')

    # User Move = Rock
    if user_move == 'r' and computer_move == 'r':
        print('It\'s a tie')
        ties = ties + 1
    elif user_move == 'r' and computer_move == 'p':
        print('You lose')
        losses = losses + 1
    elif user_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1

    # User Move = Paper
    if user_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif user_move == 'p' and computer_move == 'p':
        print('It\'s a tie')
        ties = ties + 1
    elif user_move == 'p' and computer_move == 's':
        print('You lose')
        losses = losses + 1

    # User Move = Scissor
    if user_move == 's' and computer_move == 'r':
        print('You lose')
        losses = losses + 1
    elif user_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif user_move == 's' and computer_move == 's':
        print('It\'s a tie')
        ties = ties + 1
