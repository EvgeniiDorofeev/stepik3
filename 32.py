def check_sum(*args):
    if sum(args)<50:
        print('not enough')
    else:
        print('verification passed')

check_sum(20, 20, 10)