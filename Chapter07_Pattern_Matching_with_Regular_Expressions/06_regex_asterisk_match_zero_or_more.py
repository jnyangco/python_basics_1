# * asterisk means "match zero or more"
# it can completely absent or repeated multiple times
import re

# (wo)* -> 'Batman' zero match instance
bat_regex = re.compile(r'Bat(wo)*man')
match_obj1 = bat_regex.search('The adventure of Batman.')
print(match_obj1.group())

# (wo)* -> 'Batwoman' match 1 instance
match_obj2 = bat_regex.search('The adventure of Batwoman')
print(match_obj2.group())

# (wo)* -> 'Batwowowoman' match 4 instances
match_obj3 = bat_regex.search('The adventure of Batwowowowoman.')
print(match_obj3.group())