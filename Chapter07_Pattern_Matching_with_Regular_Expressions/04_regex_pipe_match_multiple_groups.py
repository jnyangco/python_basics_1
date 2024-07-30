# The | character is called a pipe. You can use it anywhere you want to match one of many expressions.
# For example, the regular expression r'Batman|Tina Fey' will match either 'Batman' or 'Tina Fey'.
# When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned
import re

hero_regex = re.compile(r'Batman|Superman')

match_obj1 = hero_regex.search('Batman and Superman')
print(match_obj1.group())

match_obj2 = hero_regex.search('Superman and Batman')
print(match_obj2.group())


hero_regex = re.compile(r'Batman|Wonder Woman|Wolverine')
match_obj3 = hero_regex.findall('Superman, Batman, Wonder Woman and Wolverine')
print(match_obj3)  # return a list -> ['Superman', 'Batman', 'Wonder Woman']
# for item in match_obj3:
#     print(item)
print('-----------------------')


# Pipe on regex parts
# You can also use the pipe to match one of several patterns as part of your regex
# i.e: you can use it to search prefix, etc...
hero_regex = re.compile(r'Bat(man|mobile|copter|bat)')
match_obj4 = hero_regex.search('Batmobile lost its wheel')
print(match_obj4.group())
print(match_obj4.group(1))
