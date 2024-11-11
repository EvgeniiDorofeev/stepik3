def is_strings_equal(a,b):
    return sorted(a)==sorted(b)
    # print(sorted(a))
    # print(sorted(b))
    # if len(a)==len(b):
    #     for i in a:
    #         if b.index(i):
    #             break
    #         else:
    #             return False
    #     return True
    # return False
print(is_strings_equal("aalc", "aacl"))

