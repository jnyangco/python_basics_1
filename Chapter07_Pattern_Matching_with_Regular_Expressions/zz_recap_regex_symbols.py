# The ? matches zero or one of the preceding group.
# The * matches zero or more of the preceding group.
# The + matches one or more of the preceding group.
# The {n} matches exactly n of the preceding group.
# The {n,} matches n or more of the preceding group.
# The {,m} matches 0 to m of the preceding group.
# The {n,m} matches at least n and at most m of the preceding group.
# {n,m}? or *? or +? performs a non-greedy match of the preceding group.
# ^spam means the string must begin with spam.
# spam$ means the string must end with spam.
# The . matches any character, except newline characters.
# \d, \w, and \s match a digit, word, or space character, respectively.
# \D, \W, and \S match anything except a digit, word, or space character, respectively.
# [abc] matches any character between the brackets (such as a, b, or c).
# [^abc] matches any character that isn’t between the brackets.


# Summary
# While a computer can search for text quickly, it must be told precisely what to look for.
# Regular expressions allow you to specify the pattern of characters you are looking for, rather than the exact text
# itself. In fact, some word processing and spreadsheet applications provide find-and-replace features that allow you
# to search using regular expressions.
# The re module that comes with Python lets you compile Regex objects. These objects have several methods:
# search() to find a single match, findall() to find all matching instances, and sub() to do a find-and-replace
# substitution of text.
# You can find out more in the official Python documentation at https://docs.python.org/3/library/re.html.
# Another useful resource is the tutorial website https://www.regular-expressions.info/.
