from functools import wraps
def counting_calls(func):
    k=0
    calls={}
    @wraps(func)
    def inner(*args, **kwargs):
        for i in range(1):
            nonlocal k
            k += 1
        setattr(inner, 'call_count', k)
        return func(*args, **kwargs)
    
    return inner

@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(30, 5))
print(add(3, 5))
print(add(4, 5))
print('Количество вызовов =', add.call_count)
print(add(11, 5))
print('Количество вызовов =', add.call_count)