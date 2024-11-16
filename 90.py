from functools import wraps
def reverse(func):
    @wraps(func)
    def inner(*args, **kwargs):
        x=()
        if len(args) == 0:
            return
        else:
            x = list(args)
            x.reverse()
            x = tuple(x)
        return func(*x)
    return inner


def get_average(*args, **kwargs):
    summa = sum(args) + sum(kwargs.values())
    count = len(args) + len(kwargs)
    return summa / count


print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
# декорируем
get_average = reverse(get_average)
print(get_average(1, 2, 3, 4, 5, a=10, b=15, c=12))
