def print_goods(*args):
    k=0
    for i in args:
        if isinstance(i, str) and i!='':
            k+=1
            print (f'{k}. {i}')
    if k==0:
        print('Нет товаров')

print_goods(1, True, 'Грушечка', '', 'Pineapple')