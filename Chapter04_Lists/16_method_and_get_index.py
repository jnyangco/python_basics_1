spam = ['hello', 'hi', 'howdy', 'heyas']

print(spam.index('hello'))
print(spam.index('howdy'))
# print(spam.index('hello word'))  # ValueError: 'hello word' is not in list


# When there are duplicates of the value in the list, the index of its first appearance is returned
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))