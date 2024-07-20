# nested dictionary
all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def total_brought(guests, picnic_item):
    num_brought = 0
    for k, v in guests.items():  # string of the guest's name is assigned to k (which iterate for 3 times)
        num_brought = num_brought + v.get(picnic_item, 0)  # NOTE: .get(<key>, 0) need fallback 0 to avoid error
                                                            # if <key> exist in dict, return the value of that key
                                                            # if <key> does not exist in the dict, return 0
    return num_brought


print('cakes -> ' + str(total_brought(all_guests, 'cakes')))
print('apples -> ' + str(total_brought(all_guests, 'apples')))
print('pretzels -> ' + str(total_brought(all_guests, 'pretzels')))
print('ham sandwiches -> ' + str(total_brought(all_guests, 'ham sandwiches')))
print('cups -> ' + str(total_brought(all_guests, 'cups')))
print('apple pies -> ' + str(total_brought(all_guests, 'apple pies')))


# ======================================================================
# print(all_guests)
# print(all_guests.keys())
# print(all_guests.values())
# print(list(all_guests.keys()))

# for k, v in all_guests.items():
#     print('key-> ' + k)
#     print('value-> ' + str(v))
#     print('v.get-> ' v.get('apples', 0))

# RESULT:
# key-> Alice
# value-> {'apples': 5, 'pretzels': 12}
# v.get-> 5

# key-> Bob
# value-> {'ham sandwiches': 3, 'apples': 2}
# v.get-> 2

# key-> Carol
# value-> {'cups': 3, 'apple pies': 1}
# v.get-> 0