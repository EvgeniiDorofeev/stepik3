from functools import wraps
def monkey_patching(func):
    @wraps(func)
    def inner(*args, **kwargs):
        a=[]
        c={}
        for i in range(len(args)):
            #print(args[i])
            a.append('Monkey')
        for i in kwargs:
            c[i]='patching'
        return func(*a,**c)
    return inner


@monkey_patching
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    return ', '.join(args)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
print(concatenate('my', 'name is', 'Artem'))
print(concatenate.__name__)
print(concatenate.__doc__.strip())




