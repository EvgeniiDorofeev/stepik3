def filter_collection(f, lst):
    a=[]
    if type(lst)==str:
        for num in lst:
            if f(num) == True:
                a.append(num)
        w=''.join(a)
        return w
    else:
        for num in lst:
            if f(num)==True:
                a.append(num)
        return type(lst)(a)

def is_positive(num):
    return num > 0

numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
positive_numbers = filter_collection(is_positive, numbers)
print(positive_numbers)