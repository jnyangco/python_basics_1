list1 = ['hello', 'hi', 'howdy', 'heyas']

# in
print('howdy' in list1)
print('how you doing' in list1)

print('----------------')
# not
print('howdy' not in list1)
print('how you doing' not in list1)


# using inputs
print('----------------')
my_pets = ['Zophie', 'Fat-tail', 'Macbeth']
pet_name = input('Enter one of my pets name: ')
if pet_name in my_pets:
    print(pet_name + ' is one of my pets!')
else:
    print('I do not have a pet named ' +pet_name)
