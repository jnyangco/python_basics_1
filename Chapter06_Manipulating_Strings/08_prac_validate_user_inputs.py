while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        print(f'Your age is {age}.')
        break
    else:
        print('Please enter a number only.')

while True:
    print('Enter your new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        print('Password is saved!')
        break
    else:
        print('Password should only consists of letters and numbers only.')
