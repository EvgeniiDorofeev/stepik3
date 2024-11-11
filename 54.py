def print_best_and_worst_laureate(laureates):
    a={}
    for i in laureates:
        a[laureates[i]] = 0
    for i in laureates:
        if laureates[i] in a:
            a[laureates[i]]+=1
    maxim = max(a.items(), key = lambda x: x[1])
    minim =min(a.items(), key = lambda x: x[1])
    print(f'{maxim[0]}, {maxim[1]}')
    print(f'{minim[0]}, {minim[1]}')


laureates = {'За лучший фильм': 'Оппенгеймер',
             'За лучшую музыку к фильму': 'Оппенгеймер',
             'За лучший звук': 'Зона интересов',
             'За лучшие визуальные эффекты': 'Бедные-несчастные',
             'За лучший дизайн костюмов': 'Бедные-несчастные',
             'За лучшую операторскую работу': 'Бедные-несчастные',
             'За лучший монтаж': 'Оппенгеймер',
             'За лучший оригинальный сценарий': 'Оппенгеймер',
             'За лучший фильм на иностранном языке': 'Зона интересов'}

print_best_and_worst_laureate(laureates)