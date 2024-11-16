from functools import wraps
def explicit_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        #print(args)
        #print(kwargs)
        if len(args) != 0:
            return print('Вы не можете передать позиционные аргументы. Используйте именованный способ передачи значений')
        return func(**kwargs)
    return inner
@explicit_args
def add(a: int, b: int) -> int:
    '''Возвращает сумму двух чисел'''
    return a + b

print(add(10, 20))

