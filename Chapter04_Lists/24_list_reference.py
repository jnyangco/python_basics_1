# assign values + create reference in memory
spam = 42
cheese = spam
spam = 100
print(cheese)
print(spam)


# lists are mutable
spam = [0, 1, 2, 3, 4, 5]
cheese = spam  # The reference is being copied, not the list # -> values stored in spam and cheese now both refer to the same list
cheese[1] = 'Hello'  # This changes the list value

print(spam)    # [0, 'Hello', 2, 3, 4, 5]
print(cheese)  # [0, 'Hello', 2, 3, 4, 5]


