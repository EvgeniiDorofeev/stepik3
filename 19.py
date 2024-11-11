def replace(text, old, new=None):
    a=''
    for i in text:
        if i==old and new!=None:
            a=a+str(new)
        elif i==old and new==None:
            continue
        else:
            a=a+i
    return a
print(replace('Нет', 'т',))