# JOIN() -> join list of strings into a single string
# syntax: '<str>.join(['item1', 'item2', 'item3']) -> output: item1 + <str> + item2 + <str> . . .
# note: <str> acts as delimiter/separator

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('<ABC>'.join(['My', 'name', 'is', 'Simon']))
print('----------------------------------')

# 1.1 SPLIT() -> by default, split whitespace characters such as the space, tab, or newline characters are found
print('My name is Simon'.split())  # return -> ['My', 'name', 'is', 'Simon']

# 1.2 SPLIT with DELIMITER
print('My<ABC>name<ABC>is<ABC>Simon'.split('<ABC>'))


# A common use of split() is to split a multiline string along the newline characters.
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob
'''
print(spam.split('\n'))