# Regex Version of the strip() Method
# Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are
# passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the
# string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
import re

strip_regex = re.compile(r'^\s+|\s+$')
text = '   HelloWorld         '
print(len(text))

matches = strip_regex.findall(text)
print(matches)
# print(match_ojb.group())

new_text = text.replace(matches[0], '')
print(new_text)
print(len(new_text))
