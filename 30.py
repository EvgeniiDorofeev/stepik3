def count_args(*args):
    k=0
    for i in args:
        k+=1
    return k

print(count_args(1, 2, 3, 4, 5))