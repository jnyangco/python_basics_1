# str.upper()
# str.lower()
# str.isupper -> true/false
# str.islower -> true/false

spam = 'Hello, world!'

print(spam.upper())
print(spam.lower())
print(spam)

print('-------------------')
spam = spam.upper()
print(spam)
print(spam.isupper())
print(spam.islower())

print('-------------------')
print('12345'.islower())  # false
print('12345'.isupper())  # false
print('abc12345'.islower())  # true
print('12345ABC'.isupper())  # true


print('-------------------')
print('How are you?')
feeling = input()
if feeling.lower() == 'great':
    print('I feel great too!')
else:
    print('I hope the rest of your day is good.')