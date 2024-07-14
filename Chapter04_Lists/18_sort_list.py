# NOTE: sort() and reverse() does not return a value. hence do not store in a variable
# spam = spam.sort() -> spam.sort()
# spam = spam.reverse() -> spam.reverse()


# 1.1 list.sort()
spam = [2, 10, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
print(spam)

# 1.2 list.sort(reverse=True)
spam.sort(reverse=True)
print(spam)

# note: cannot sort list with both string and integers
# spam = [1, 3, 2, 4, 'Alice', 'Bob']
# spam.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print('--------------------------------------------------------')
# 3.1 note: sort() uses "ASCIIbetical order" rather than actual alphabetical order for sorting strings
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)  # result -> ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

# 3.2 sort(key=str.lower)
# if you need to sort the values in regular alphabetical order, pass str.lower
# for the key keyword argument in the sort() method call
spam.sort(key=str.lower)  # or -> # spam.sort(reverse=True, key=str.lower)
print(spam)


print('--------------------------------------------------------')
# 4 REVERSE
spam.reverse()
print(spam)