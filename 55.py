def print_order_rating(drivers):
    a = {}
    for i,j in drivers:
        if i in a:
            a[i].append(j)
        else:
            a[i] = []
            a[i].append(j)
    for i in a:
        a[i]=sum(a[i])/len(a[i])
    b = sorted(a.items(), key=lambda x: (-x[1],x[0].lower()))
    for s,d in b:
        print(f'{s} {d}')



drivers = [
    ('Джек', 2),
    ('Джек', 3),
    ('Гермиона', 5),
    ('Билл', 4),
    ('Билл', 4),
    ('Гермиона', 3),
    ('Джек', 2),
    ('ЯЯ', 5),
    ('ФФФ', 5),
    ('Билл', 4),
    ('Укк', 4),
    ('Билл', 3),
    ('Джек', 2),
    ('Джек', 2),
    ('Гермиона', 5),
    ('Билл', 2),
    ('ФФФ', 4),
    ('Билл', 3),
    ('ФФФ', 3),
    ('Джек', 2),
    ('Джек', 1),
    ('Гермиона', 5),
    ('Билл', 2),
    ('Курт', 5),
    ('Билл', 3),
]
print_order_rating(drivers)