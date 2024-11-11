def validate_all_args_str(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, str) for arg in args):
            return func(*args, **kwargs)
        print('Все аргументы должны быть строками')
    return wrapper




def validate_all_kwargs_int_pos(func):
    a=''
    def func(*args, **kwargs):
        nonlocal a
        for i in args:
            a=a+str(i)
        for i in kwargs:
            if type(kwargs[i]) is int and kwargs[i]>0:
                a = a + str(kwargs[i])
            else:
                print('Все именованные аргументы должны быть положительными числами')
                return
        return a
    return func
#iuhuh
@validate_all_args_str
@validate_all_kwargs_int_pos
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result

print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))