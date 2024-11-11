def count_strings(*args):
    k=0
    for i in args:
        if isinstance(i, str):
            k+=1
    return k

print(count_strings(1, 2, 'hello', True, 't'))