# . -> any single character except newline
# * -> zero or more of the preceding character
# .* -> match anything (greedy mode) - python matches the shortest string
# .*? -> match anything (non-greedy fashion) - python matches the longest string
import re

# .*
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match_obj = name_regex.search('First Name: John Last Name: Doe')
print(match_obj.group())
print(match_obj.group(1))
print(match_obj.group(2))

# r'<.*?>' -> question mark tells python to match in a non-greedy way
non_greedy_regex = re.compile(r'<.*?>')
match_obj = non_greedy_regex.search('<To serve man> for dinner.>')
print(match_obj.group())  # <To serve man>

greedy_regex = re.compile(r'<.*>')
match_obj = greedy_regex.search('<To serve man> for dinner.>')
print(match_obj.group())  # <To serve man> for dinner.>
