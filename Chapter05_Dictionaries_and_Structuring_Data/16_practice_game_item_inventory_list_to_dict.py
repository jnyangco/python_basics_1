# character_stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(stuff):
    print('Inventory:')
    total_items = 0
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        total_items = total_items + v
    print('Total number of items: ' + str(total_items))


def add_to_inventory(inventory, list_items):
    for i in list_items:
        if i in inventory.keys():
            # print(i)
            # print(inventory[i])
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
    return inventory


dict_inventory = {'gold coin': 42, 'rope': 1}
list_dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

dict_inventory = add_to_inventory(dict_inventory, list_dragon_loot)

display_inventory(dict_inventory)