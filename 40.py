def truncate_sentences(n, *args):
    for i in args:
        print (i[0:n])



truncate_sentences(
        8,
        "Мой дядя самых честных правил,",
        "Когда не в шутку занемог,",
        "Он уважать себя заставил"
    )