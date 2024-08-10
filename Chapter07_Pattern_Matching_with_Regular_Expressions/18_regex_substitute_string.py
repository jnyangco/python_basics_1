# sub() method returns a string with the substitutions applied
# two arguments
# 1st arg -> a string to replace any matches
# 2nd arg -> the string for the regular expression
import re

name_regex = re.compile(r'Agent \w+')
match_obj = name_regex.sub('SUPER', 'Agent Alice gave the secret documents to Agent Bob.')
print(match_obj)  # SUPER gave the secret documents to SUPER.

match_obj = name_regex.sub('SUPER', 'Test Alice gave the secret documents to Test Bob.')
print(match_obj)  # NO Match -> return original string

secret_name_regex = re.compile(r'Agent (\w)\w*')
# match_obj = secret_name_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
match_obj = secret_name_regex.sub(r'Agent \1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(match_obj)

