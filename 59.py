def create_attrs(obj, x):
    for i in x:
        setattr(obj, i[0], i[1])
def check_exist_attrs(obj, x):
    a={}
    for i in x:
        a[i]=hasattr(obj, i)
    return a

def print_goods(lst):
    pass

create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])

print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))

