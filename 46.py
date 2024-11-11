def rotate(lst : list[int | float], shift:int=1)->list[int | float]:
    'Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)'
    a=[]
    k=0
    shift=shift%len(lst)
    if shift>0:
        for i in range(len(lst),0,-1):
            a.append(lst[-shift+k])
            k+=1
    else:
        for i in range(len(lst),0,-1):
            a.append(lst[-shift+k])
            k+=1
    return a

print(rotate.__doc__)
print(rotate.__annotations__)
print(rotate([1, 2, 3, 4, 5, 6], -3))