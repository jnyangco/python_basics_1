# Python regular expressions -> greedy by default (will match the longest string possible)
# Non-greedy -> also called lazy version of the braces (will match the shortest string possible) followed by question mark ?
import re

# return longest(maximum) match -> HaHaHaHaHa
greedy_ha_regex = re.compile(r'(Ha){3,5}')
match_obj1 = greedy_ha_regex.search('HaHaHaHaHa')
print(match_obj1.group())


# return shortest(minimum) match -> HaHaHa
# end curly braces followed by ? -> (Ha){3,5}?
nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
match_obj2 = nongreedy_ha_regex.search('HaHaHaHaHa')
print(match_obj2.group())

