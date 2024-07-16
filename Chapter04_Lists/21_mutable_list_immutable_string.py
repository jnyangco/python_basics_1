# Immutable String
name = 'Zophie a cat'
new_name = name[0:6] + ' the ' + name[9:12]
print(new_name)
# name[0:6] = 'Daphie' # TypeError: 'str' object does not support item assignment


# Mutable List
eggs = [1, 2, 3]
eggs[0] = 0
eggs.append(4)
eggs.append(5)
del eggs[4]
eggs.insert(1, 100)

print(eggs)
