def create_dict():
    count=0
    a={}
    def inner(x):
        nonlocal count
        count+=1
        a[count]=x
        return a
    return inner


f_1 = create_dict()
print(f_1('privet'))
print(f_1('poka'))
print(f_1([5, 2, 3]))

f2 = create_dict()
print(f2(5))
print(f2(15))

