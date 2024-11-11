def wrap_increment(value):
    def _inc(x):
        return x+1


    return _inc(value)

print(wrap_increment(41))