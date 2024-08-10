# re.VERBOSE -> ignore whitespace and comments inside the regular expression
import re

# hard to read
# phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

# you can spread the regular expression over multiple lines with comments like this:
phoneRegex = re.compile(r'''
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE -> using pipe '|'
# what is you want to use re.VERBOSE to write comments in your regular expression?
# but also want to use re.IGNORECASE to ignore capitalization?


some_regex_value = re.compile('foo', re.IGNORECASE | re.DOTALL)
some_regex_value = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)