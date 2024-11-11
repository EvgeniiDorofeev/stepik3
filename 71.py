def aggregation(f, lst):
    a=[]
    k=lst[0]
    for i in lst[1:]:
        a.append(f(k,i))
        k=f(k,i)
    return a



def get_max(x, y):
    return max(x, y)

# агрегируем нахождение максимума
print(aggregation(get_max, [1, 4, 5, 7, 6, 5, 8, 10]))