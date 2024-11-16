from functools import wraps
def limit_query(N):
    def decorator(func):
        k=0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal k
            if k>=N:
                return print(f'Лимит вызовов закончен, все {N} попытки израсходованы')
            k+=1
            return func(*args, **kwargs)
        return wrapper
    return decorator


@limit_query(3)
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add(10, 33))
print(add.__name__)