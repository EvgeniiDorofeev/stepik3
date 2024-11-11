def print_scores(name, *args):
    print('Student name:', name)
    a=sorted(args)
    for i in a:
        print(i)
print_scores("Jud", 100, 95, 88, 92, 99)