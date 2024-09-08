
import time, sys
indent = 0
indent_increase = True

try:
    while True:
        if indent_increase:
            print(' ' * indent, end='')
            print('**********')
            indent += 1

            if indent == 10:
                indent_increase = False
        else:
            print(' ' * indent, end='')
            print('**********')
            indent -= 1

            if indent == 0:
                indent_increase = True

        time.sleep(0.10)

except KeyboardInterrupt:
    print('Program Exit.')
    sys.exit()
#
# print('' * 10, 'Hello')