# by default - regular expression match text with exact casing
import re

# re.IGNORECASE or re.I
# re.compile(r'<regex_here>', re.IGNORECASE)

robocop_regex = re.compile(r'robocop', re.IGNORECASE)
match_obj = robocop_regex.search('RoboCop is half man and half machine, all cop.')
print(match_obj.group())

match_obj = robocop_regex.search('ROBOCOP protects the innocent.')
print(match_obj.group())

