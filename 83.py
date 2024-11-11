def repeater(func):
    def inner(*args,**kwargs):
        for i in range(3):
            res=func(*args,**kwargs)
    return inner
@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(9, 4)