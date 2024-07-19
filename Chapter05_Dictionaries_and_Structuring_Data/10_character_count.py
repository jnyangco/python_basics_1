message = 'HelloWorld'

# dictionary
dict_char_count = {}

for character in message:
    dict_char_count.setdefault(character, 0)  # add key-value to dictionary if not exist, if exist return current value

    # key = value
    dict_char_count[character] = dict_char_count[character] + 1  # dict['key'] = dict['key'] + 1


print(dict_char_count)

