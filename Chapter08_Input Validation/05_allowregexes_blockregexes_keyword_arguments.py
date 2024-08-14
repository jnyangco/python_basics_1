import pyinputplus as pyip

# 1. Allow Regexes
# try input -> XLII
response = pyip.inputNum(prompt='#1.1 Allow Regex -> Enter a number: ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')

# try input -> xlii
response = pyip.inputNum(prompt='#1.2 Allow Regex -> Enter a number: ', allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')


# 2. Block Regexes
# 0-5 are blocked
response = pyip.inputNum(prompt='#2 Block Regex -> Enter a number: ', blockRegexes=[r'[012345]$'])
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')


# 3. Allow List overrides Block List
# note: It will allow 2 words, but everything that has 'cat' in the word will be blocked i.e: 'cater', 'catcat', etc..
response = pyip.inputStr(prompt='#3 Enter text: ', allowRegexes=[r'caterpillar', 'category'], blockRegexes=[r'cat'])
print(f'response = {response}')
print(f'type = {type(response)}')
print('-----------------------')