def compute(x,*args):
    a=[]
    for r in x:
        for t in args:
            a.append(r(t))
    return a

def square(num):
    return num ** 2

def inc(num):
    return num + 1

def dec(num):
    return num - 1

print(compute([inc, dec, square], 10, 20, 30, 40))