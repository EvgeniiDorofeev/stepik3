def is_member(value, lst):
    for i in lst:
        if i==value:
            return True
    return False
def overlapping(a,b):
    for i in a:
        if is_member(i,b):
            return True
    return False
print(overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))