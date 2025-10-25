

expected_items = ["Dog", "Cat", "Bird"]
actual_items = ["Dog", "Mice", "Bird"]

print("---------------------")
for item in enumerate(actual_items):
    print(item)
# (0, 'Dog')
# (1, 'Mice')
# (2, 'Cat')

print("---------------------")
for item in enumerate(actual_items):
    print(item[0])
# 0
# 1
# 2

print("---------------------")
for item in enumerate(actual_items):
    print(item[1])
# Dog
# Mice
# Cat

print("---------------------")
for index, item in enumerate(actual_items):
    print(f"index = {index}")
    print(f"actual_item = {item}, expected_item = {expected_items[index]}")
# Dog
# Mice
# Cat