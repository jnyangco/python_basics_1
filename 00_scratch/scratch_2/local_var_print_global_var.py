
def spam():
    global eggs
    print(eggs)
    eggs = 'hello'
    print(eggs)

eggs = 'global eggs'
spam()