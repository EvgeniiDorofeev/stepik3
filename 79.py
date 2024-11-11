def count_calls():
    n=0
    def inner():
        nonlocal n
        inner.total_calls=1+n
        n=inner.total_calls
    inner.total_calls = 0
    return inner



counter = count_calls()
counter()
counter()
print(counter.total_calls)
counter()
print(counter.total_calls)