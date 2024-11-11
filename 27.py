def words_length(words):
    for i, x in enumerate(words):
        words[i] = len(x)
    return None

words = ['Python', 'is', 'awesome!']
result = words_length(words)
print(words)
print(result)