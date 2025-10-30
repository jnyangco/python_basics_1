# empty string     -> False -> all other value considered True
# number 0 or 0.0  -> False -> all other value considered True

name = ''

while not name:  # checking if empty string -> (if empty = True)
    print('Enter your name: ')
    name = input()



# ================================================================
print('How many guest do you have?')
number_of_guest = int(input())

if number_of_guest:  # (not 0 or 0.0) -> True, if value is 0 or 0.0 -> means False
    print('Be sure to have enough room for all your guests.')

print('Done!')