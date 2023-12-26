from itertools import combinations


def hash_(seq: str) -> int:
    a = 1000
    m = 123987123
    len_ = len(seq) - 1
    sum_ = 0
    for i, char in enumerate(seq):
        sum_ += (a ** (len_ - i) * ord(char))
    return sum_ % m


res = {}
for count in range(7, 27):
    for s in combinations('qwertyuioplkjhgfdsazxcvbnm', count):
        s = ''.join(s)
        h = hash_(s)
        if h in res:
            print(res[h])
            print(s)
            print(h)
            raise ValueError
        else:
            res[h] = s
