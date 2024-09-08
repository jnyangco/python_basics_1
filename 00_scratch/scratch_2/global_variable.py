
def spam():
    global eggs
    eggs = 'local eggs'


eggs = 'global eggs'

spam()
print(eggs)