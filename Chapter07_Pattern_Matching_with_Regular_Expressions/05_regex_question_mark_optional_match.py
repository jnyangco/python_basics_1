# Sometimes there is a pattern that you want to match optionally -> using ? question mark
import re

# (wo)? part of the regular expression means that the pattern wo is an optional group
bat_regex = re.compile(r'Bat(wo)?man')
match_obj = bat_regex.search('Batwoman')
print(match_obj.group())
print('-----------')

phone_regex = re.compile(r'\(?\d\d\d\)?-\d\d\d-\d\d\d\d')
match_obj = phone_regex.search('415-555-4242')
print(match_obj.group())

match_obj = phone_regex.search('(415)-555-4242')
print(match_obj.group())
print('-----------')


phone_regex = re.compile(r'(\(\d\) )?\d\d\d-\d\d\d-\d\d\d\d')
match_obj = phone_regex.search('(1) 415-555-4242')
print(match_obj.group())

match_obj = phone_regex.search('415-555-4242')
print(match_obj.group())

