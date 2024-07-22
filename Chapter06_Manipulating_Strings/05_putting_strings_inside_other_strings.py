name = 'Al'
age = 4000
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')

# STRING INTERPOLATION using curly brackets {} -> no need to convert int to str()
print('My name is {}. I am {} years old.'.format(name, age))

# F STRING -> place variable inside the curly braces -> print(f'Hello {name}')
print(f'My name is {name}. Next year I will be {age + 1}')
