def calculate_per_person(p,n, s=10):
    return round((p+(p/100*s))/n, 2)

print(calculate_per_person(100.0, 5, 0))