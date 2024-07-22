# The partition() method is useful for splitting a string whenever you NEED the PARTS BEFORE,
# including, and after a particular separator string.

# SPLIT STRING using PARTITION method
print('Hello, world!'.partition('w'))  # tuple? -> ('Hello, ', 'w', 'orld!')
print('Hello, world!'.partition('world'))  # tuple? -> ('Hello, ', 'world', '!')

# MULTIPLE -> if the string appears to be multiple, it will split but only the first occurrence will be returned
print('Hello, world!'.split('o'))  # list? -> ['Hell', ', w', 'rld!']

# String NOT found -> If the separator string can’t be found,
# the first string returned in the tuple will be the entire string, and the other two strings will be empty:
print('Hello, world! Test Hello 1234'.partition('XYZ'))  # ('Hello, world! Test Hello 1234', '', '')


# Tuple - multiple assignment trick
before, delimiter, after = 'Hello, world!'.partition(' ')
print(before)
print(delimiter)
print(after)
