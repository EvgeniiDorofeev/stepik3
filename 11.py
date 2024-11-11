def is_member(value, lst):
    for i in lst:
        if i==value:
            return True
    return False
print(is_member("e", ['a', 'e', 'i', 'o', 'u']))