spam = ['cat', 'bat', 'rat', 'elephant']

# select range
print(spam[0:1])
print(spam[1:3])

spam_sub2 = spam[0:3]
# print(spam_sub2[3])  # error: list index out of range

# using negative index -> useful when you want to slice from end of the list
print("-------------------")
print(spam[0:-1])  # 0:4 (4 - 1 = 3) -> [0:3]
print(spam[0:-2])  # 0:4 (4 - 2 = 2) -> [0:2]


# blank index
print(spam[0:])
print(spam[:4])
