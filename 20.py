def deco(flow):
    def hafiz(*args, **kwargs):
        '''This is decorator'''
        print('God bless you')
        return flow(*args, **kwargs)
    return hafiz

@deco
def add(a):
    '''This is below function'''
    return 2 * a

print(add(5)) 