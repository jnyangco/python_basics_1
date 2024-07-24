# Sometimes you may want to strip off whitespace characters (space, tab, and newline)
# from the left side, right side, or both sides of a string

spam = '        Hello, World        '
print('>' + spam.strip() + '<')
print('>' + spam.lstrip() + '<')
print('>' + spam.rstrip() + '<')


# STRIP with Argument
# Passing strip() the argument 'ampS' will tell it to strip occurrences of a, m, p, and capital S from the ends of the
# string stored in spam.
# The order of the characters in the string passed to strip() does not matter: strip('ampS')
# will do the same thing as strip('mapS') or strip('Spam').
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))
print(spam.strip('mapS'))
print(spam.strip('pamS'))
print(spam.strip('Spam'))
