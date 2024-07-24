# These functions are useful when you need to do an ordering or mathematical operation on characters:
# Get text Unicode code point
print(ord('A'))  # return an integer (unicode point)
print(ord('4'))
print(ord('!'))

print(chr(65))  # return the character (of the unicode point)
print(chr(52))
print(chr(33))


print('-----------------')
print(ord('B'))
print(ord('A') < ord('B'))
print(ord('D') < ord('C'))


print('-----------------')
print(chr(65))
print(chr(ord('A') + 1))