def apply(x, y):
    return [x(num) for num in y]


def square(num):
    return num ** 2


print(apply(square, [5, 7, 0, 3]))