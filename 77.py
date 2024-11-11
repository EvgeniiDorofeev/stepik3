def create_accumulator(k=0):
    def inner(r):
        nonlocal k
        k=k+r
        return k
    return inner

summator_1 = create_accumulator(200)
print(summator_1(5))
print(summator_1(7))
print(summator_1(2))

summator_2 = create_accumulator()
print(summator_2(3))
print(summator_2(6))