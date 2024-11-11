alpha = 'abcdefghijklmnopqrstuvwxyz'
import string
def is_pangram(x):
    x=x.lower().replace(' ','').translate(str.maketrans('', '', string.punctuation))
    print(x)
    return all([i in x for i in alpha])
print(is_pangram("The quick brown fox jumps over the lazy dog."))
