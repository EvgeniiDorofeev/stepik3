def info_kwargs(**kwargs):
    a=sorted(kwargs)
    for i in a:
        print(f'{i}={kwargs[i]}')

info_kwargs(c=43, b= 32, a=32)