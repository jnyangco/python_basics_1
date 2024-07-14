# Instead of using the range(len(someList)) technique with a for loop to obtain the integer index of the items in the list,
# you can call the enumerate() function instead

supplies = ['pens', 'staplers', 'papers', 'binders']
for index, item in enumerate(supplies):
    print('index ' + str(index) + ' in supplies is: ' + item)

# The enumerate() function is useful if you need both the ITEM and the ITEM'S INDEX in the loop's block.