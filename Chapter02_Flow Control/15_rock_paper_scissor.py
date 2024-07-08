import random
import sys

wins = 0
losses = 0
ties = 0

while True:  # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    # print('{} Wins, {} Losses, {} Ties'.format(wins, losses, ties))

    while True:  # Player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input()
        if player_move == 'q':
            sys.exit()  # quit the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break  # break out of the player input loop
        print('Invalid input, enter one of (r), (p), (s), or (q).')

    # Display what the player chose:
    if player_move == 'r':
        print('[ROCK vs ', end='')
    elif player_move == 'p':
        print('[PAPER vs...', end='')
    elif player_move == 's':
        print('[SCISSORS vs...', end='')

    # Display what the computer chose:
    # random_number = random.randint(1, 3)
    # if random_number == 1:
    #     computer_move = 'r'
    #     print('ROCK')
    # elif random_number == 2:
    #     computer_move = 'p'
    #     print('PAPER')
    # elif random_number == 3:
    #     computer_move = 's'
    #     print('SCISSORS')

    # Display what the computer chose:
    computer_move_list = ('r', 'p', 's')
    computer_move = random.choice(computer_move_list)
    # print(computer_move)
    if computer_move == 'r':
        print('ROCK]')
    elif computer_move == 'p':
        print('PAPER]')
    elif computer_move == 's':
        print('SCISSORS]')

    # Display and record the win/loss/tie:
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1

    elif player_move == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1

    elif player_move == 'r' and computer_move == 'p':
        print('You lose!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lose!')
        losses = losses
    elif player_move == 's' and computer_move == 'r':
        print('You lose!')