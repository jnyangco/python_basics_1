import copy

spam = ['A', 'B', 'C', 'D']
print(id(spam))

cheese = copy.copy(spam)  # Now the spam and cheese variables refer to separate lists
print(id(cheese))  # cheese is a different list with different identity
cheese[1] = 42  # it will change cheese list only, spam will not change

print(spam)
print(cheese)


# hello = [(1, 2, 3, 4), ('X', 'Y', 'Z')]
# print(hello)
# copy.deepcopy(hello)
# hello[0] = 10
# print(hello)

