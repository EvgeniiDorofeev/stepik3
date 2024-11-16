def multiply_result_by(N):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)*N
        return wrapper
    return decorator
@multiply_result_by(3)
@multiply_result_by(4)
def my_function(x, y):
    return x + y


print(my_function(2, 3))