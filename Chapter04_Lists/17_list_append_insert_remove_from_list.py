# APPEND
# list.append(item here)
list1 = ['cat', 'dog', 'bat']
list1.append('moose')
print(list1)

# INSERT
# list.insert(index, item here) -> insert item before index
list2 = ['pens', 'staplers', 'papers']
list2.insert(1, 'binders')
print(list2)

# REMOVE -> using Value
# list.remove(item)
list1.remove('moose')
list1.remove('bat')
print(list1)

# list.remove(item) not exist -> ValueError: .. x not in list
# list1.remove('elephant')

# If the value appears multiple times in the list, only the first instance of the value will be removed
list3 = ['A', 'B', 'B', 'C', 'D']
list3.remove('B')
print(list3)

# REMOVE -> using Index -> list3.__delitem__
list3.__delitem__(-1)
print(list3)