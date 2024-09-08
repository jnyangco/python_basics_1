import sys

def division(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print('Program Error.')
        return None  # by default


print(division(10, 2))
print(round(division(10, 3), 4))
print(division(10, 0))