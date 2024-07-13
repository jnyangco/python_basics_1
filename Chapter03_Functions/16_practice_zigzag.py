import time, sys
indent = 0 # How many spaces to indent
indent_increasing = True  # Whether the indentation is increasing or not

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        # print('********')
        print('************************')
        time.sleep(0.01) # Pause for 1/10 of a second

        if indent_increasing:
            # Increase number of spaces
            indent = indent + 1
            if indent == 20:
                indent_increasing = False # Change direction

        else:
            # Decrease number of spaces
            indent = indent - 1
            if indent == 0:
                indent_increasing = True # Change direction
except KeyboardInterrupt:
    sys.exit()
