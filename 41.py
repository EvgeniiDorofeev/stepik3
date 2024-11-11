def make_strings_big(*args, reverse=False):
    if reverse==False:
        for i in args:
            print(i.upper())
    else:
        for i in args:
            print(i.lower())

make_strings_big('У лукоморья дуб зелёный',
                     'Златая цепь на дубе том:',
                 "И днём и ночью кот учёный")