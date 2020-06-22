

def outer_func(msg):
    def inner_func():
        print(f'Inner func function')
        msg()
        print(f'Inner func function')
    return inner_func

def decan():
    print(f'Inside decoreto !!!!!!!!!')

c = outer_func(decan)

c()