from functools import wraps
def check_count_args(func):
    k=0
    @wraps(func)
    def inner(*args, **kwargs):
        for i in range(len(args)):
            nonlocal k
            k += 1
        for j in range(len(kwargs)):
            k+=1
        if k<2:
            return print('Not enough arguments')
        elif k>2:
            return print('Too many arguments')
        else:
            return func(*args, **kwargs)
    return inner

@check_count_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y

add_numbers(3, 5, 6)