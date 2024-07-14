# multiple assignment trick (technically called tuple unpacking) is a shortcut that lets you assign multiple variables
# with the values in a list in one line of code

# long -> assign variables using list values
# cat = ['small', 'gray', 'meows']
# size = cat[0]
# color = cat[1]
# sound = cat[2]

# short (tuple) -> assign variables using list values
dog = ['big', 'brown', 'woof']
size, color, sound = dog
for i in range(len(dog)):
    print(dog[i])