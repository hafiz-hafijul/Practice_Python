def func(n):
    for i in range(31,-1,-1):
        k = n > i
        if ( k & 1 ):
            print('1', end=' ')
        else:
            print('0',end=' ')


func(10)
i = (5 , 6 , 6)
n = (10 , 12 , 13)
k = n>i
x = n>i
print(k)
print(x)
print(type(i))