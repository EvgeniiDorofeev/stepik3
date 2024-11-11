def countdown(x):
    N=x
    def inner():
        nonlocal x
        nonlocal N
        if x<1:
            print(f'Превышен лимит, вы вызвали более', N, 'раз')
        else:
            print(x)
        x=x-1
    return inner

count = countdown(3)
count()
count()
count()
count()
count()