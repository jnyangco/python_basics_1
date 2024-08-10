# Strong Password Detection
# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase
# characters, and has at least one digit. You may need to test the string against multiple regex patterns to
# validate its strength.
import re

# password_regex = re.compile(r'(\d+|\w+){8,15}')
# password_regex = re.compile(r'[a-zA-Z0-9]{8,9}')

# password_regex = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')
# At least one upper case English letter, (?=.*?[A-Z])
# At least one lower case English letter, (?=.*?[a-z])
# At least one digit, (?=.*?[0-9])
# At least one special character, (?=.*?[#?!@$%^&*-])
# Minimum eight in length .{8,} (with the anchors)


password_regex = re.compile(r'^(.{0,7}|[^0-9]*|[^A-Z]*|[^a-z]*|[a-zA-Z0-9]*)$')
# Regular expressions don't have an AND operator, so it's pretty hard to write a regex that matches valid passwords,
# when validity is defined by something AND something else AND something else...
# But, regular expressions do have an OR operator, so just apply DeMorgan's theorem,
# and write a regex that matches invalid passwords:
# Anything with less than eight characters OR anything with no numbers OR anything with no uppercase
# OR or anything with no lowercase OR anything with no special characters.
# If anything matches that, then it's an invalid password

print('Enter your password: ')
# password = input()
password = 'eHowossd'

match_obj = password_regex.search(password)
print(match_obj.group())
