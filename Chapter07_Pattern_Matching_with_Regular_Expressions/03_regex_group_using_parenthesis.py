
import re

# group regex by parenthesis
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

matched_objects = phone_number_regex.search('My number is 415-555-4242.')
print(matched_objects.group(1))
print(matched_objects.group(2))
print(matched_objects.group(0))  # group() or group(0) -> return entire match
print('---------------------------')


# .groups() -> plural - retrieve all the groups at once -> will return tuple
# can use tuple unpacking
print(matched_objects.groups())  # return -> ('415', '555-4242')
area_code, main_number = matched_objects.groups()
print(f'area code -> {area_code}')
print(f'main number -> {main_number}')
print('---------------------------')

# using parenthesis as regular expression -> use escape characters '\( \)'
# note: you still need to use escape characters even you're using raw strings
# .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
# \.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)
phone_number_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
matched_objects = phone_number_regex.search('My number is (415)-555-4242.')
print(matched_objects.group(1))
print(matched_objects.group(2))
print(matched_objects.group())
