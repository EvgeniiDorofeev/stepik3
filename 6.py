def is_leap(n):
    if n%4==0 and n%100!=0:
        return True
    if n%400==0:
        return True
    return False
def get_leap_years(y1,y2):
    k=[]
    for i in range(y1,y2):
        if is_leap(i):
            k.append(i)
    return k
print(get_leap_years(2000, 2018))