def find_longest_word_len(s):
    k=0
    for i in s:
        if len(i)>k:
            k=len(i)
    return k
print(find_longest_word_len(['default', 'ghostwriter', 'bother', 'applaud', 'skate', 'way']))