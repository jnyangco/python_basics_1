table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# len = 3

print([0] * len(table_data))

def print_table(data):
    max_col_width = 0
    column = []

    for x in range(len(data)):
        print([0] * len(table_data))

        for y in range(len(data[0])):
            column.append(data[x][y])
            if len(data[0][y]) > max_col_width:
                max_col_width = len(data[0][y])
                print(f'max col width {max_col_width}')
            # column = column + data[x][y]
            # print(data[x][y], end='')
        # print('\n')
    print(column)


print_table(table_data)
