# \d -> shorthand for the regular expression (0|1|2|3|4|5|6|7|8|9)
# Character classes are nice for shortening regular expressions
import re

# Shorthand Codes for Common Character Classes
# \d -> any numeric digit from 0 to 9
# \D -> any character that is NOT a numeric digit from 0 to 9
# \w -> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W -> Any character that is not a letter, numeric digit, or the underscore character.
# \s -> Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S -> Any character that is not a space, tab, or newline.

xmas_regex = re.compile(r'\d+\s\w+')
# will match text that has ONE OR MORE numeric digits (\d+)
# followed by a (ONE) whitespace character (\s),
# followed by (ONE OR MORE) letter/digit/underscore characters (\w+)

# output -> ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans']

# xmas_regex = re.compile(r'\d*\s\w*')
# output -> ['12 drummers', ' 11', ' pipers', ' 10', ' lords', ' 9', ' ladies', ' 8', ' maids', ' 7', ' swans']

match_ojb = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids 7 swans')
print(match_ojb)
