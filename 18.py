def translate_to_robber_lang(x):
    s=['a', 'e', 'i', 'o', 'u']
    k=[]
    for i in x:
        if i in s:
            k.append(i)
    return ''.join(k)
print(translate_to_robber_lang("This is kinda fun"))