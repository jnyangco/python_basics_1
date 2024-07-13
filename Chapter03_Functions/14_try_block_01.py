def spam(divide_by):
    try:
        return 20 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid input, cannot divide by zero.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

