def create_actor(**kwargs):
    a={'name': 'Райан', 'surname': 'Рейнольдс', 'age': 47}
    for i, j in kwargs.items():
        a[i]=j
    return a

actor = create_actor(height=190,movies=['Дедпул', 'Главный герой'])
print(actor)

