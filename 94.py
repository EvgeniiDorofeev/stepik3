from functools import wraps
def cache_result(func):
    cache={}
    @wraps(func)
    def inner(*args,**kwargs):
        res=func(*args,**kwargs)
        if tuple(args) in cache:
            print(f'[FROM CACHE] Вызов {func.__name__} = {res}')
        if tuple(kwargs) in cache:
            print(f'[FROM CACHE] Вызов {func.__name__} = {res}')
        cache[args or tuple(kwargs)] = res
        return func(*args,**kwargs)
    return inner



@cache_result
def multiply(a, b):
    return a * b


print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(4, 5))
print(multiply(5, 4))
print(multiply.__name__)