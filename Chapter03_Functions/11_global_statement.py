# Note: If you ever want to modify the value stored in a global variable from a function,
# you must use a global statement on that variable.

def spam():
    global eggs  # this will access global var 'eggs' and modify value
    eggs = 'local eggs'


eggs = 'global eggs'

spam()
print(eggs)