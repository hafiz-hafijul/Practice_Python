def deco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@deco
def gloo(x):
    return 20 * x


print(gloo(20))
