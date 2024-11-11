def create_tuples(a,b):
    c=[]
    k=0
    for i in a:
        for j in b:
            s=i,b[k]
            k+=1
            c.append(s)
            break
    return c
print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))