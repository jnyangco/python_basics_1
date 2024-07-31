# .* -> match everything except newline \n character
# Include Newline Character -> By passing re.DOTALL as the second argument to re.compile()
# you can make the dot character match all characters, including the newline character

import re

no_newline_regex = re.compile('.*')  # will match everything only up to the first newline \n character
match_obj = no_newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(match_obj)

newline_regex = re.compile('.*', re.DOTALL)  # match everything including newline \n characters
match_obj = newline_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(match_obj)

