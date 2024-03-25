import sys


def prefix(s: str) -> list:
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p


def main():
    s = sys.stdin.readline().strip()
    p = sys.stdin.readline().strip()
    r = sys.stdin.readline().strip()
    prf = prefix(f'{p}#{s}')
    n = len(p)
    res = []
    prev = 0
    for i, count in enumerate(prf[n*2:]):
        if count == n:
            res.append(s[prev:i])
            res.append(r)
            prev = i + n
    res.append(s[prev:])
    print(''.join(res))


main()
