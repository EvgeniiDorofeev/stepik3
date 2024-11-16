from functools import wraps
def monkey_patching(arg='Monkey', kwarg='patching'):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            a=[]
            c={}
            for i in range(len(args)):
                a.append(arg)
            for i in kwargs:
                c[i]=kwarg
            return func(*a,**c)
        return inner
    return decorator


@monkey_patching(kwarg='Duper', arg='Super')
def print_args_kwargs(*args, **kwargs):
    for i, value in enumerate(args):
        print(i, value)
    for k, v in sorted(kwargs.items()):
        print(f'{k} = {v}')

print_args_kwargs(1, 2, 3, 4, b=300, w=40, t=50, a=100)




