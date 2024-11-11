def make_repeater(x):
    def inner(r):
        return r*x
    return inner


repeat_5 = make_repeater(5)
print(repeat_5('Hello'))
print(repeat_5('World'))

repeat_2 = make_repeater(2)
print(repeat_2('Pizza'))
print(repeat_2('Pasta'))