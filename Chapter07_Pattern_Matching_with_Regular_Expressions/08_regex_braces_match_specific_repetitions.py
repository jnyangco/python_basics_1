# (Ha){3} -> match HaHaHa
# (Ha){3} -> not match HaHa
import re

# (Ha){<min>,<max>}
ha_regex = re.compile(r'(Ha){3}')
match_obj1 = ha_regex.search('HaHaHa')
print(match_obj1.group())

match_obj2 = ha_regex.search('Ha')
print(f'Ha is None -> {match_obj2 is None}')
print('------------')

ha_regex = re.compile(r'(Ha){1,3}')
match_obj1 = ha_regex.search('Ha')
print(match_obj1.group())
print(f'Ha is None -> {match_obj1 is None}. Ha is True')

match_obj2 = ha_regex.search('HaHa')
print(match_obj2.group())

match_obj2 = ha_regex.search('HaHaHa')
print(match_obj2.group())

match_obj2 = ha_regex.search('HaHaHaHaHaHaHaHa')  # it will only match 3x HaHaHa. {1,3} 3 is the maximum
print(match_obj2.group())
