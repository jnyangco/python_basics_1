birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# dictionary['key'] -> access dictionary value
# dictionary['key'] = 'value' -> add key value pair to dictionary

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(name + ' birthday is on ' + birthdays[name])
    else:
        print('I do not have birthday information for ' + name)
        print('Enter birthday to save: ')
        save_birthday = input()
        birthdays[name] = save_birthday
        print('Birthday database updated.')
