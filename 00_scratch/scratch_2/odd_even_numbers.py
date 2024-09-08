number = input('Enter a number: ')

print('\nPrinting even numbers: ')
for i in range(int(number) + 1):
    if i % 2 == 0:
        print(i)

print('\nPrinting odd numbers: ')
for i in range(int(number) + 1):
    if i % 2 != 0:
        print(i)
