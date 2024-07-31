# You can use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of searched text
# Likewise, you can put a dollar sign ($) at the end of the regex to indicate the string must end with this regex pattern
# And you can use the ^ and $ together to indicate that the entire string must match the regex
import re

# 1. BEGIN -> r'^Hello' -> matches strings that begin with 'Hello'
begins_with_hello_regex = re.compile(r'^Hello')
match_obj = begins_with_hello_regex.search('Hello, world!')
print(match_obj)  # match Hello

match_obj = begins_with_hello_regex.search('He said Hello.')
print(match_obj)  # None


# 2. END -> r'\d$' -> matches strings that end with a numeric character from 0 to 9
ends_with_number_regex = re.compile(r'\d$')
match_obj = ends_with_number_regex.search('Your number is 42')
print(match_obj)  # match 2

match_obj = ends_with_number_regex.search('42 is your number')
print(match_obj)  # None


# 3. BEGIN + END -> r'^\d+$'
whole_string_is_number = re.compile(r'^\d+$')
match_obj = whole_string_is_number.search('1234567890')
print(match_obj) # match 1234567890

match_obj = whole_string_is_number.search('12345xyz67890')
print(match_obj) # None