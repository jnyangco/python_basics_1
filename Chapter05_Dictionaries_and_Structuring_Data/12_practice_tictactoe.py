# dict_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#              'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#              'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

dict_board = {'top-L': '0', 'top-M': '0', 'top-R': '0',
             'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}



def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


# print_board(dictionary)
print_board(dict_board)