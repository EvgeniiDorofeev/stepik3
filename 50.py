def  factorial(n):
    k=1
    global a
    if n in a:
        print(f'Get from cache value factorial({n})')
    for i in range(1,n+1):
        k*=i
    a.update({n:k})
    return k

a={}

print(factorial(5))
print(factorial(6))
print(factorial(5))