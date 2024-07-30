# Note: is<method> is useful to validate user inputs
# isalpha() -> if string consists of only letters
# isdecimal() -> if string consists only numeric numbers and is not blank

# note: isnumber() and isdigit() accepts other type of strings (i.e: "0 3 8", "0.3.8", etc...)

# isalnum() -> if string consists of letters and numbers

# isspace() -> if string consists only of spaces, tabs, and newlines and is not blank
# istitle() -> if string consists only of words that begin with an upper case letter followed by only lowercase letters


print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())

print('--------------------------')
print('123'.isdecimal())  # True
print('123.5'.isdecimal())  # False -> Why?
print('Test')
print('123'.isnumeric())  # True
print('123.5'.isnumeric())  # False

print('--------------------------')
print('                 '
      ''.isspace())

print('--------------------------')
print('This Phrase Only Has Title Case'.istitle())  # True
print('123 This Is Title Case'.istitle())  # True
print('This is Not a Title Case'.istitle())  # False
print('This Is NOT A Title Case'.istitle())  # False