
# long code
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam.keys():
    spam['color'] = 'black'
    spam['color'] = 'white'  # this will override key-value even if it is already exist
print(spam)
print('------------------')


# ADD ITEM TO DICTIONARY -> EXISTED OR NOT
print(spam.setdefault('color', 'black'))  # if key not exist, add key-value to dict
print(spam)  # {'name': 'Pooka', 'age': 5, 'color': 'black'}

print(spam.setdefault('color', 'white'))  # if key exist, will NOT add key-value to dict (it will return the CURRENT VALUE)
print(spam)


# note: setdefault() method is a nice shortcut to ensure that a key exists