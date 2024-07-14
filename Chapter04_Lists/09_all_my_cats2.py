
# declare list with no values
cat_names = []

while True:
    print('Enter the name of the cat ' + str(len(cat_names) + 1))
    cat_name = input()  # 1 item
    if cat_name == '':
        break
    cat_names = cat_names + [cat_name]  # concat -> need to wrapped in a bracket

# print('The cat names are: ' + str(cat_names))
print('The cat names are: ')
for i in range(len(cat_names)):
    print(cat_names[i])

# sample inputs:
# Zophie
# Pooka
# Simon
# Lady Macbeth
# Fet-tail
# Miss Cleo