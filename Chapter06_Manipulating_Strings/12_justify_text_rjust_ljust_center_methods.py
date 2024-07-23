# These methods are especially useful when you need to print tabular data that has correct spacing


# Add padding with total number of strings

# .rjust(<width str>), .ljust(), center()
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello'.ljust(20) + 'world!')
print('---------------------------')

# With 2ND ARGUMENT -> (<width>, fillchar)
print('Hello'.rjust(10, '*'))
print('Hello'.ljust(10, '*'))
print('Hello'.ljust(10, '-') + 'world!')
print('---------------------------')


# .center(<width>), .center(<width>, fillchar)
print('Hello'.center(20))
print('Hello'.center(20, '-'))