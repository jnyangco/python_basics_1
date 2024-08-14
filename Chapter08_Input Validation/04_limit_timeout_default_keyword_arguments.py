import pyinputplus as pyip

# will throw an error after 2x incorrect input
response = pyip.inputNum(prompt='Enter a number: ', limit=2)
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')

# will throw an error if you enter after the given seconds
response = pyip.inputNum(prompt='Enter a number: ', timeout=5)
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')

# default -> after incorrect limit, it will return the default value you set
response = pyip.inputNum(prompt='Enter a number: ', limit=2, default='You have reached incorrect input limits.')
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')