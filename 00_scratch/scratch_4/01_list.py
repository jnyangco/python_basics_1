
list_number = [1, 2, 3, 4, 5]
list_string = ['cat', 'dog', 'mice']
list_diff_data = [1, 'cat', True, None]

print(list_number)
print(list_string)
print(list_diff_data)

for i in list_number:
    print(i)

for s in list_string:
    print(s)

for i in range(len(list_string)):
    print(list_string[i])

for i in range(len(list_diff_data)):
    print(list_diff_data[i])