# find every phone number and email address on a very long webpage or document
# Step: Select Text -> CTRL+C -> process the clipboard -> CTRL+V -> Boom!
import re
import pyperclip

# High level flow:
# 1. Get the text off the clipboard
# 2. Find all phone numbers and email addresses in the text
# 3. Paste them onto the clipboard

# Code flow:
# 1. Use the pyperclip module to copy and paste strings
# 2. Create two regexes for phone numbers and for email addresses
# 3. Find all matches, not just the first match, ob both regexes
# 4. Neatly format the matched strings into a single string to paste
# 5. Display some kind of message if no matches were found in the text

text_document = '''The quick brown fox jumps over the lazy dog
Here are the list of phone numbers and email addresses:
1. 511-111-2348     test_one1234@google.com
2. 522-222-8756     test_two2345@google.com
3. 533-333-0913     test_three3874@google.com
4. 544-444-7653     test_four1058@google.com
5. 555-555-1859     test_five7827@google.com
'''

# > Append to a List Variable
# > Join list using \n and print

# 1. GET CLIPBOARD TEXT -> variable = pyperclip.paste()
# clipboard_text = pyperclip.paste()
# text_document = clipboard_text


# 2. REGEX for Phone and Email
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
email_regex = re.compile(r'\w+@google.com')

# 3. PROCESS TEXT
match_phone = phone_regex.findall(text_document)
match_email = email_regex.findall(text_document)
# print(match_phone)
# print(match_email)

print_clipboard_text = []
for i, phone in enumerate(match_phone):
    print(str(i+1) + '.' + phone)
    print_clipboard_text.append(phone)

print('---------------------------------')
for i, email in enumerate(match_email):
    print(str(i+1) + '.' + email)
    print_clipboard_text.append(email)

# phone_regex.search()

# text = 'TEST1234'
# 4. PASTE TO CLIPBOARD -> paste text to the Clipboard -> Ready to paste (Cmd + V)
pyperclip.copy('\n'.join(print_clipboard_text))
# print(pyperclip.copy(print_clipboard_text))
