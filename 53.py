def print_goods(data):
    txt=[]
    for i in data:
        a,b=i.split(':')
        b=float(b)
        c=(b,a)
        txt.append(c)
    txt.sort(key=lambda x: (-x[0], x[1].lower()))
    for price, name in txt:
        print(f'{price:.2f} - {name}')


data = [
    'Sony PlayStation 5: 46000.5',
    'Телевизор QLED Samsung QE65Q60TAU: 87090',
    'Samsung Galaxy s23: 46000.5',
    'siemens eq.6 plus s100: 46000.5',
    'Samsung Galaxy Tab S6: 46000.5',
]
print_goods(data)