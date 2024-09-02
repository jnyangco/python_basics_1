# empty string     -> False -> all other value considered True
# number 0 or 0.0  -> False -> all other value considered True


name = ''

while not name:  # while not (means if empty string) -> False
    print('Enter your name: ')
    name = input()

print('How many guest do you have?')
number_of_guest = input()

if number_of_guest:  # (not 0 or 0.0) -> True, if value is 0 or 0.0 -> means False
    print('Be sure to have enough room for all your guests.')

print('Done!')