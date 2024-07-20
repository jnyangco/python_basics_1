character_stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(stuff):
    print('Inventory:')
    total_items = 0
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        total_items = total_items + v
    print('Total number of items: ' + str(total_items))


display_inventory(character_stuff)
