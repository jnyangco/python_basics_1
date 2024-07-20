all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}


def get_total_of_item(guest, item):
    total_item = 0
    for k, v in guest.items():
        total_item = total_item + v.get(item, 0)
    return total_item


print('apples -> ' + str(get_total_of_item(all_guests, 'apples')))
print('cups -> ' + str(get_total_of_item(all_guests, 'cups')))