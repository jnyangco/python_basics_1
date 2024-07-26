#! python3
# bullet_point_adder.py - Add Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()
# text = 'List of animals\nList of aquarium life\nList of biologists by author abbreviation\nList of cultivars'

# Separate lines and add starts
lines = text.split('\n')  # "List of animals\nList of aquarium life\nList of biologists by author abbreviation\nList of cultivars"
for i in range(len(lines)):
    # lines[0] = '* List of animals'
    lines[i] = '* ' + lines[i]

# join() list of items in 1 string -> '<separator>'.join(list)
text = '\n'.join(lines)
text = text.upper()
# print(text)


# copy text to the Clipboard -> Ready to paste (Cmd + V)
pyperclip.copy(text)





# Even if you don’t need to automate this specific task, you might want to automate some other kind of text manipulation,
# such as removing trailing spaces from the end of lines or converting text to uppercase or lowercase.
# Whatever your needs, you can use the clipboard for input and output.

