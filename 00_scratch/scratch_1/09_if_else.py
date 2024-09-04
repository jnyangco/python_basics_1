name = input('Enter your username: ')


if name.lower() == 'john':
    password = input('Enter your password: ')

    if password == 'Password@1':
        print('You are now logged-in!')
    else:
        print('You entered incorrect password. Try again.')
else:
    print('Invalid username.')