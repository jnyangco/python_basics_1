spam = ['cat', 'bat', 'rat', 'elephant']

# List length
print(len(spam))


for i in range(len(spam)):
    print(spam[i])

print('---------------------------')
# list change item value
spam[0] = spam[1]
spam[-1] = spam[2]
for i in range(len(spam)):
    print(spam[i])

print('---------------------------')
print(spam)
spam = spam + [1, 2, 3]
print(spam)