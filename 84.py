def double_it(func):
    def inner(*args,**kwargs):
        res=func(*args,**kwargs)*2
        return res
    return inner


@double_it
def get_sum_kwargs_values(**kwargs):
    return sum(kwargs.values())


print(get_sum_kwargs_values(a=4, b=5, c=7))
print(get_sum_kwargs_values(a=4, b=5, d=3, t=6, r=8))