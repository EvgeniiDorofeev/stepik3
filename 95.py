from functools import wraps
def counting_calls(func):
    k = 0
    calls = []
    a={}
    b={}
    c={}
    @wraps(func)
    def inner(*args, **kwargs):
        for i in range(1):
            nonlocal k
            k += 1
        setattr(inner, 'call_count', k)
        a['args']=args
        b['kwargs']=kwargs
        c.update(a)
        c.update(b)
        calls.append(c)
        setattr(inner, 'calls', calls)
        return func(*args, **kwargs)
    return inner


@counting_calls
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, b=20))
print(add(7, 5))
print(add(12, 45))
print('Количество вызовов =', add.call_count)
print(add.calls[2])

print(add(b=11, a=22))
print(add.calls[3])