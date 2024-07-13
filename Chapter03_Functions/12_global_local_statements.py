# Note: If you ever want to modify the value stored in a global variable from in a function,
# you must use a global statement on that variable.

def spam():
    global eggs
    eggs = 'spam'  # change global variable


def bacon():
    eggs = 'bacon'  # this is a local


def ham():
    print(eggs)  # this is the global


eggs = 42  # this is global variable
spam()
print(eggs)