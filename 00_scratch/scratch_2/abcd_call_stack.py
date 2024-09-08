def a():
    print('Start A')
    b()
    print('End A')


def b():
    print('Start B')
    c()
    print('End B')


def c():
    print('Start C')
    d()
    print('End C')


def d():
    print('Start D')
    print('End D')


a()
