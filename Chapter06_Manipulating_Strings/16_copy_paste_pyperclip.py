import pyperclip

pyperclip.copy('Hello, world!')
print(pyperclip.paste())

# Of course, if something outside of your program changes the clipboard contents, the paste() function will return it.
# i.e: copy this text "For example, if I copied this sentence to the clipboard and then called paste()"

# the print it using pyperclip.paste()
# print(pyperclip.paste())
