def register_check(a):
    k=0
    for i in a:
        if a[i]=='yes':
            k+=1
    return k
people = {'Igor': 'yes', 'Stas': 'no', 'Peter': 'no', 'Mary': 'yes'}
print(register_check(people))