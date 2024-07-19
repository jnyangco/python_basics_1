picnic_items = {'apples': 5, 'cups': 2}

# dict.get('key', <fallback value>)
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')


# not using .get() -> it will cause a KeyError: 'eggs'
print('I am bringing ' + str(picnic_items['eggs']) + ' eggs.')