def aggregation(f, lst, initial=None):
    a=[]
    if initial!=None:
        k=f(initial,lst[0])
    else:
        k=lst[0]
    for i in lst[1:]:
        k=f(k,i)
    return k



print(aggregation(lambda x, y: x + y, [4, 5, 6], initial=100))