def concatenate(**kwargs):
    a=[]
    for i in kwargs:
        a.append(str(kwargs[i]))
    a=''.join(a)
    return a


print(concatenate(t='Happy', y="Meal", w="Cost", m=10, b='Buks'))