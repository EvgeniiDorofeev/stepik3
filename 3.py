def is_leap(n):
    if n%4==0 and n%100!=0:
        return True
    if n%400==0:
        return True
    return False