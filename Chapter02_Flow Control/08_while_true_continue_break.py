while True:
    print('What is your username: ')
    name = input()

    if name != 'John':
        continue # it will jump back to the start of the loop

    print('Hello, John. What is your password: (Hint: it is a fish.)')
    password = input()
    if password == 'swordfish':
        break # it will jump out of the loop
    print('Incorrect password, jumps back to start of the loop.')

print('Access granted!')

print()
print()