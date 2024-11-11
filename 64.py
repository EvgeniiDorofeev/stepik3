def double_odd_numbers(numbers):
    def double(x):
        return x*2
    def is_odd(x):
        return x%2!=0


    return [double(num) for num in numbers if is_odd(num)]

print(double_odd_numbers([1, 2, 3, 4, 5]))