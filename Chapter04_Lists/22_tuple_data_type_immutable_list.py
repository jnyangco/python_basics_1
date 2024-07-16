# The tuple data type is almost identical to the list data type, except in two ways.
# First, tuples are typed with parentheses -> ( ) instead of square brackets [ ]

eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))


# But the main way that tuples are different from lists is that tuples, like strings, are immutable.
# Tuples cannot have their values modified, appended, or removed.
eggs = ('hello', 42, 0.5)
# eggs[1] = 99 # -> TypeError: 'tuple' object does not support item assignment


# If you have only one value in your tuple -> you can indicate this by placing a trailing comma after the first value
# Otherwise, Python will think you’ve just typed a value inside regular parentheses
tuple1 = ('hello',)  # type -> tuple
tuple2 = ('hello')   # type -> string
print(type(tuple1))
print(type(tuple2))


# USAGE:
# You can use tuples to convey to anyone reading your code that you don’t intend for that sequence of values to change.
# -> cannot use reassignment of each items

# If you need an ordered sequence of values that never changes, use a tuple.
# -> cannot use SORT

# A second benefit of using tuples instead of lists is that, because they are immutable and their contents don’t change,
# Python can implement some optimizations that make code using tuples slightly faster than code using lists.
