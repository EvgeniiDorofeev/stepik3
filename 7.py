def is_palindrome(n):
    s=n.lower()
    k=''.join(s.split())
    a=k[::-1]
    return k==a
def create_palindrome(k):
    if is_palindrome(k):
        return k.lower()
    else:
        d=k.lower()+'_i_'+k[::-1].lower()
        return d
print(create_palindrome('Hello'))