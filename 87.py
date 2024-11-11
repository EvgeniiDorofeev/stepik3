def validate_all_args_str(func):
    a=''
    def func(*args, **kwargs):
        #print(kwargs)
        nonlocal a
        for i in args:
            if type(i)==str:
                a=a+i
            else:
                print('Все аргументы должны быть строками')
                return
        for i in kwargs:
            #if type(kwargs[i])==str:
            a = a + str(kwargs[i])
        return a
    return func

@validate_all_args_str
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "думаю", "Выучить", "Питон", a="За", b=10, c="Месяцев"))