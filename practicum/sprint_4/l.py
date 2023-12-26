import sys


def main():
    n, k = input().split()
    n = int(n)
    k = int(k)

    seq = sys.stdin.readline().rstrip()

    counts = {}
    stopped = set()
    for i in range(n - 1, len(seq)):
        substring = seq[i - n: i]
        if substring in stopped:
            continue
        res = counts.get(substring, (0, i - n))
        if res[0] + 1 >= k:
            stopped.add(substring)
            print(res[1], end=' ')
            counts.pop(substring)
            continue
        counts[substring] = res[0] + 1, res[1]

    for count, i in counts.values():
        if count >= k:
            print(i, end=' ')


main()
