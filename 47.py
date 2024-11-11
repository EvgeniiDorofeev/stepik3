def rotate(tpl : tuple[int | float, ...], shift:int=1)->tuple[int | float, ...]:
    'Функция выполняет циклический сдвиг кортежа на shift позиций вправо (shift>0) или влево (shift<0)'
    a=[]
    k=0
    shift=shift%len(tpl)
    if shift>0:
        for i in range(len(tpl),0,-1):
            a.append(tpl[-shift+k])
            k+=1
    else:
        for i in range(len(tpl),0,-1):
            a.append(tpl[-shift+k])
            k+=1
    return tuple(a)

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate((1, 2, 3, 4, 5, 6, 7), 2))