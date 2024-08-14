import pyinputplus as pyip

response = input('#1 > Enter a number: ')
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')

response = pyip.inputInt(prompt='#2 > Enter a number: ')
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')

# input can be blank, need param set to True -> blank=True
response = pyip.inputInt(prompt='#2 > Enter a number: ', blank=True)
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')