# search() will return a Match object of the first matched text ONLY in the searched string
# findall() method will return the strings (form of LIST) of every match in the searched string
import re

# search()
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_obj1 = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(match_obj1.group())  # search() only return the first matched text

# findall() -> return all matched strings as long as there is no group in regular expression
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
match_obj1 = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(match_obj1.group())  # AttributeError: 'list' object has no attribute 'group', get values not using .group()
print(match_obj1)  # ['415-555-9999', '212-555-0000']

# findall()
# note: If there are groups in the regular expression, then findall() will return a list of tuples (one string for each group)
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has no groups
match_obj1 = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
# print(match_obj1.group())  # AttributeError: 'list' object has no attribute 'group', get values not using .group()
print(match_obj1)  # [('415', '555', '9999'), ('212', '555', '0000')]
