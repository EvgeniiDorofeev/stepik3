def aggregation(f, lst):
    a=[]
    k=lst[0]
    for i in lst[1:]:
        k=f(k,i)
    return k



def get_add(x, y):
    return x + y


print(aggregation(get_add, [5, 2, 4, 3, 5]))