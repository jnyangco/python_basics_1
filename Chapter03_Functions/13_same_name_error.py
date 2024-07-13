def spam():
    print(eggs)  # ERROR!
    eggs = 'local'


eggs = 'global'
spam()