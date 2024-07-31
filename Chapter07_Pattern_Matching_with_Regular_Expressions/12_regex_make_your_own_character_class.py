# regex in a square brackets
# syntax -> re.compile(r'[<regex_here>]')

# There are times when you want to match a set of characters but the shorthand character classes (\d, \w, \s, and so on)
# are too broad. You can define your own character class using square brackets.
# For example, the character class [aeiouAEIOU] will match any vowel, both lowercase and uppercase.
import re

# [aeiouAEIOU]
vowel_regex = re.compile(r'[aeiouAEIOU]')
match_obj = vowel_regex.findall('#1 RoboCop eats baby food. #2 BABY FOOD.')
print(match_obj)


# [a-zA-Z0-9] -> will match all lowercase letters, uppercase letters, and numbers
# You can also include ranges of letters or numbers by using a hyphen
# Note that inside the square brackets, the normal regular expression symbols are not interpreted as such.
# This means you do not need to escape the ., *, ?, or () characters with a preceding backslash.
letters_digits_upper_lower_regex = re.compile(r'[a-zA-Z0-9]')
match_obj = letters_digits_upper_lower_regex.findall('#1 RoboCop eats baby food. #2 BABY FOOD.')
print(match_obj)

# [0-5.] -> will match digits 0 to 5 and a period (no need to write it as [0-5\.]
digits_one_to_five_regex = re.compile(r'[0-5]')
match_obj = digits_one_to_five_regex.findall('#1234 RoboCop eats baby food. #5678 BABY FOOD.')
print(match_obj)


# [^aeiouAEIOU]
# CARET ^ -> negative character (NOT)
# just after the character class’s opening bracket, you can make a negative character class.
# A negative character class will match all the characters that are not in the character class
consonant_regex = re.compile(r'[^aeiouAEIOU]')
match_obj = consonant_regex.findall('#1 RoboCop eats baby food. #2 BABY FOOD.')
print(match_obj)