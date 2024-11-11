def is_leap(n):
    if n%4==0 and n%100!=0:
        return True
    if n%400==0:
        return True
    return False
def count_leap_years(y1,y2):
    k=0
    for i in range(y1,y2):
        if is_leap(i):
            k+=1
    return k
print(count_leap_years(2015, 2020))