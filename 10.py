def filter_long_words(s,n):
    a=[]
    for i in s:
        if len(i)>n:
            a.append(i)
    return a
print(filter_long_words(['sister', 'arena', 'formal', 'arena', 'spill'], 5))