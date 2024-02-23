import sys


def main():
    input()
    seq = sys.stdin.readline().rstrip().split()
    match = {'0': -1, '1': 1}
    max_len = len(seq)
    result = sum(match[value] for value in seq)
    l = 0
    r = len(seq) - 1
    exp = '1' if result < 0 else '0'
    while l != r:
        if result == 0:
            return max_len
        if seq[l] == exp:
            result -= match[exp]
            l += 1
        else:
            result -= match[seq[r]]
            r -= 1
        max_len -= 1

    return 0


print(main())
