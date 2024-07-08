# Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

print('-------------------')
for i in range(1, 11):
    print(i)

print('-------------------')
i = 1
while True:
    print(i)
    if i == 10:
        break
    i = i + 1

