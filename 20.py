def product(a, start=1):
    k=start
    for i in a:
        k*=i
    return k
print(product([1, 2, 3], start=10))

