def find_keys(**kwargs):
    k=[]
    for i in kwargs.items():
        if isinstance(i[1], (list, tuple)):
            k.append(i[0])
    return sorted(k, key=lambda x: x.lower())


print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))