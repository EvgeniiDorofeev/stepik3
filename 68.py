def compute(x,*args):
    a=[]
    for t in args:
        f=t
        for r in x:
            f=r(f)
        a.append(f)
    return a

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, square, dec], 10, 20, 30, 40))