def calculate_high_low_avg(*args, log_to_console=False):
    a=(int(max((args))+int(min(args)))/2)
    if log_to_console:
        return (f'high={max(args)}, low={min(args)}, avg={a}\n' f'{a}')
    return a
avg = calculate_high_low_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)