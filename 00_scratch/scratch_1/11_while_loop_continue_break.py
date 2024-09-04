
name = ''

while True:
    name = input('Enter your name: ')
    if name.lower() != 'john':
        continue

    # code executed here - means name is now correct
    password = input('Enter your password: ')
    if password != 'fish1234':
        continue
    break
print('Program ended.')
