def uppercase_elements(func):
    def wrapper(*args,**kwargs):
        res = func(*args, **kwargs)
        a=[]
        b={}
        #print(res)
        #print(type(res))
        if type(res)==list:
            for i in res:
                if type(i)==str:
                    a.append(i.upper())
                else:
                    a.append(i)
            return a
        else:
            for i in res:
                #print(i)
                if type(i)==str:
                    s=res.get(i)
                    i=i.upper()
                    #print(i)
                    b[i]=s
                else:
                    s = res.get(i)
                    b[i]=s
            return b
    return wrapper


@uppercase_elements
def my_func(name, surname):
    return ['temple', 'store', name, surname, *[1, 2, 3]]

print(my_func('Gerard', 'Pique'))


def uppercase_elements(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        ---допишите здесь логику декоратора---

    return wrapper