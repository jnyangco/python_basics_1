# * -> means "match zero or more" -> Optional
# + -> means "match one or more" -> NOT Optional
import re

bat_regex = re.compile(r'Bat(wo)+man')  # at least one 'wo' is required by the plus sign
match_obj1 = bat_regex.search('The Adventures of Batwoman')
print(match_obj1.group())

match_obj2 = bat_regex.search('The Adventures of Batwowowowoman')
print(match_obj2.group())

match_obj3 = bat_regex.search('The Adventures of Batman')
print(match_obj3 == None)
# print(match_obj3.group()) -> error because it is None

