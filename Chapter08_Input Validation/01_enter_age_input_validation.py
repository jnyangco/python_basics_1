
while True:
    print('-------------------------------')
    print('Enter your age: ', end='')
    age = input()

    try:
        age = int(age)
    except:
        print('Please use numeric digits only.')
        continue

    if age < 1:
        print('Please enter a positive number.')
        continue
    break

print(f'Your age is {age}')
