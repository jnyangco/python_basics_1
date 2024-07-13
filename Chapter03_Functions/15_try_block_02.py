def spam(divide_by):
    return 20 / divide_by


try:
    print(spam(2))
    print(spam(12))
    print(spam(0))  # Error -> run will jump to except block
    print(spam(1))  # this will never run
except ZeroDivisionError:
    print('Error: Invalid input, cannot divide by zero.')

