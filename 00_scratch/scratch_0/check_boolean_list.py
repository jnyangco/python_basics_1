bool_list1 = []

bool_list1.append(False)
bool_list1.append(True)
bool_list1.append(True)

print(all(bool_list1))
print(any(bool_list1))


print("=====================")
bool_list2 = []
bool_list2.append(True)
bool_list2.append(False)

print(bool_list2)

test1 = any(bool_list1)
print(test1)