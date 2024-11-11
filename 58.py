def check_exist_attrs(obj, x):
    a={}
    for i in x:
        a[i]=hasattr(obj, i)
    return a

def print_goods(lst):
    pass

print_goods.is_working = False
print_goods.status = 'Not ready'

print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))