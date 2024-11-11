def is_palindrome(n):
    s=n.lower()
    k=''.join(s.split())
    a=k[::-1]
    return k==a
print(is_palindrome("Never Odd or Even"))