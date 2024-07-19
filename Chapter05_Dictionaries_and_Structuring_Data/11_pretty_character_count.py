# pprint.pprint() function is especially helpful when the dictionary itself contains nested lists or dictionaries.

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
dict_char_count = {}

for character in message:
    dict_char_count.setdefault(character, 0)
    dict_char_count[character] = dict_char_count[character] + 1


# SAME RESULTS - just different syntax
pprint.pprint(dict_char_count)
# print(pprint.pformat(dict_char_count))

# output:
# {' ': 13,
#  ',': 1,
#  'A': 1,
#  'I': 1,
# .......
#  's': 3,
#  't': 6,
#  'w': 2,
#  'y': 1}
