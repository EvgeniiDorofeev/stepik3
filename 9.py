def words_length(n):
    a=[]
    for i in n:
        a.append(len(i))
    return a
print(words_length(['Python', 'is', 'awesome!']))