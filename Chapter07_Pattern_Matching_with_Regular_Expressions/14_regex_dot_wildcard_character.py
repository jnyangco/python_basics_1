# . (or dot) -> a wildcard and will match any SINGLE character except for a newline
import re

dot_at_regex = re.compile(r'.at')
match_obj = dot_at_regex.findall('The cat in the hat sat on the flat mat.')
print(match_obj)  # ['cat', 'hat', 'sat', 'lat', 'mat']

