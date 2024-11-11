def filter_list(f, lst):
    a=[]
    for num in lst:
        if f(num)==True:
            a.append(num)
    return a


def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_list(is_even, numbers) # берем только четные
print(even_numbers)