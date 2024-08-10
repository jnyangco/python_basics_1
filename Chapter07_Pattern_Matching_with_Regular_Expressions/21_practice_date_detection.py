# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format. Assume that the days range from 01 to 31,
# the months range from 01 to 12, and the years range from 1000 to 2999. Note that if the day or month is a single
# digit, it’ll have a leading zero.
import re

# The regular expression doesn’t have to detect correct days for each month or for leap years; it will accept
# nonexistent dates like 31/02/2020 or 31/04/2021. Then store these strings into variables named month, day, and year,
# and write additional code that can detect if it is a valid date. April, June, September, and November have 30 days,
# February has 28 days, and the rest of the months have 31 days. February has 29 days in leap years. Leap years are
# every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible
# by 400. Note how this calculation makes it impossible to make a reasonably sized regular expression that can
# detect a valid date.

date_text = '01/01/2004'

# date_regex = re.compile(r'\d{1,2}\/\d{1,2}\/\d{2,4}')
date_regex = re.compile(r'(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0,1,2])\/(19|20)\d{2}')
# date_regex = re.compile(r'''
#     (0[1-9]|[12][0-9]|3[01])    # days 01 to 31
#     \/
#     (0[1-9]|1[0,1,2])           # month 01 to 12
#     \/
#     (19|20)\d{2}              # year in 1900 and 2000
#     ''')


matched_obj = date_regex.search(date_text)
print(matched_obj)


# Many times, you’ll be accepting just one date in your input. In that case,
# you have to specify the start and end of a string with caret (^) and dollar sign ($).
# ^(3[01]|[12][0-9]|0?[1-9])(\/|-)(1[0-2]|0?[1-9])\2([0-9]{2})?[0-9]{2}$

# REGEX:
# ^ denotes the start of the string

# (3[01]|[12][0-9]|0?[1-9]) represents the day
# -> 3[01] matches numbers from 30 to 31
# -> [12][0-9] matches numbers from 10 to 29
# -> 0?[1-9] matches numbers from 1 to 9, with an optional leading zero

# (\/|-) matches either a forward slash (/) or a hyphen (-)

# (1[0-2]|0?[1-9]) represents the month part
# -> 1[0-2] matches numbers from 10 to 12
# -> 0?[1-9] matches numbers from 1 to 9, with an optional leading zero

# \2 is a backreference that matches the same delimiter captured in the second capturing group (\/|-)
# This ensures that the delimiter between day and month is consistent

# ([0-9]{2})? matches the two-digit year part optionally
# ([0-9]{2}) matches any two digits representing a year
# [0-9]{2} matches the last two digits of the year
# $ denotes the end of the string
