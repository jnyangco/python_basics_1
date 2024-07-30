# 415-555-4242
# \d -> is a digit character
# \d\d\d-\d\d\d-\d\d\d\d -> is the regular expression for a phone number pattern
# \d\d\d-\d\d\d-\d\d\d\d = \d{3}-\d{3}-\d{3}


# 1 - Create Regex Objects
# re.compile(r'<pass reg expression pattern here>') -> use raw string r'< >'
# re module -> has all the regex functions - need to import
import re
# phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # now the phone_number_regex variable contain a Regex object
phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')  # they are the same

# 2 - Matching Regex Objects
# .search() -> return the matched object, return None if regex not found -> will only search for the first match
# .group() -> method will return the actual matched text from the searched string
match_objects = phone_number_regex.search('My number is 415-555-4242.')
print(f'matched objects - {match_objects}')
print('Phone number found: ' + match_objects.group())


