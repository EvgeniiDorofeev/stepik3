def print_statistic(data):
    a = {}
    for i,j in data:
        if i in a:
            if j in a[i]:
                continue
            else:
                a[i].append(j)
        else:
            a[i] = []
            a[i].append(j)
    #print(a)
    for i in a:
        a[i]=len(a[i])
    #print(a)
    b = sorted(a.items(), key=lambda x: (-x[1], x[0].lower()))
    for i,j in b:
        print(f'Количество уникальных комментаторов у {i} - {j}')

data = [
    ('7', 'opushka'),
    ('1', 'opushka'),
    ('2', 'opushka'),
    ('3', 'opushka'),
    ('2', 'opushka'),
    ('1', 'opushka'),
    ('2', 'opushka'),
    ('5', 'opushka'),
    ('6', 'opushka'),
    ('6', 'opushka'),
]

print_statistic(data)