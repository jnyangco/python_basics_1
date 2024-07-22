# spam = 'That is Alice cat.'
# spam = "That is Alice's cat."

# ESCAPE CHARACTERS -> backslash
# \' -> single quote
# \" -> double quote
# \t -> tab
# \n -> new line (line break)
# \\ -> backslash

spam = 'Say hi to Bob\'s mom.'
print(spam)  # Say hi to Bob's mom.
print("Hello there!\nHow are you?\nI\'m doing fine.")


# RAW STRINGS -> completely ignores all escape characters and prints any backslash that appears in the string
# print(r'<string or string with backslash>)
print(r'That is Carol\'s cat. \" \n \t \\')
print('-------------------------------------')


# MULTILINE STRINGS -> with TRIPLE SINGLE QUOTES
# While you can use the \n escape character to put a newline into a string, it is often easier to use multiline strings
# Note: Escaping single or double quote are optional in multiline strings
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')

# using regular print with multiple new line is harder to compose
# print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
