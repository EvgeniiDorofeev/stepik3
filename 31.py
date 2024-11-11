def multiply(*args):
    k=1
    for i in args:
        k*=i
    return k

print(multiply(1, 2, 3, 4, 5, 6))
