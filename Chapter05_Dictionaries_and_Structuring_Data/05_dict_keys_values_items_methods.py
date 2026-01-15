spam = {'color': 'red', 'age': 42}

# iterates over each KEYS in the dictionary
for keys in spam.keys():  # dict.keys()
    print(keys)


# iterates over each VALUES in the dictionary
for value in spam.values():  # dict.values()
    print(value)


# iterates over each ITEMS in the dictionary
for i in spam.items():  # dict.items() -> ('color', 'red') ('age', 42) -> like Tuples of key and value
    print(i)


# True list -> pass its list-like using list(dictionary)
print(spam.keys())  # -> dict_keys(['color', 'age'])
print(list(spam.keys())) # -> ['color', 'age'] -> takes the dict_keys value returned from keys() and passes it to list()



