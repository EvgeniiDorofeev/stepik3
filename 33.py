def is_only_one_positive(*args):
    k=0
    for i in args:
        if i>0:
            k+=1
    if k==1:
        return True
    else:
        return False
print(is_only_one_positive(1))