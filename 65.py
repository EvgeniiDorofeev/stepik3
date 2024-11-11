def calculate(x, y, operation):
    def addition(x,y):
        print(x+y)
    def subtraction(x,y):
        print(x-y)
    def division(x,y):
        if y!=0:
            print(x/y)
        else:
            print('На ноль делить нельзя!')
    def multiplication(x,y):
        print(x*y)
    if operation=='a':
        addition(x,y)
    elif operation=='s':
        subtraction(x,y)
    elif operation=='d':
        division(x,y)
    elif operation=='m':
        multiplication(x,y)
    else:
        print('Ошибка. Данной операции не существует')

calculate(1, 2, 'a')
