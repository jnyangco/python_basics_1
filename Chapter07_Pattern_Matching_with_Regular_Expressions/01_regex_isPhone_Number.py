# Regular Expressions specify a pattern of text to search for
# Regexes -> descriptions for a pattern of text

# US Phone Number pattern
# <three numbers> - <three numbers> - <four numbers>
# Criteria:
# Length = 12 -> i.e: 415-555-4242


def isPhoneNumber(text):
    # check if length = 12, if not return false
    if len(text) != 12:
        return False

    # check first 3 characters is a number
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    # check if 4th character is hyphen
    if text[3] != '-':
        return False

    # check second 3 characters is a number
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    # check if 8th character is hyphen
    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


# print('Is 415-555-424 a phone number?')
# print(isPhoneNumber('415-555-4242'))
#
# print('Is Moshi moshi a phone number?')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    # loop over the message by chunk of 12 characters and check
    # i=0 [0:12], i=1 [1:13], i=2 [2:14]
    chunk = message[i:i+12]
    print(chunk)

    # pass chunk to isPhoneNumber() to see if it matches a phone number
    if isPhoneNumber(chunk):
        print('Phone number found -> ' + chunk)

print('Done!')


# While the string in message is short in this example, it could be millions of characters long
# and the program would still run in less than a second
