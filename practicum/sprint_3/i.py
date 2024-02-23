import sys
from collections import defaultdict


def must_common(arr: list, k: int):
    t = defaultdict(int)
    max_ = 0
    for i in arr:
        t[i] += 1
        max_ = max(max_, t[i])

    bucket = [[] for _ in range(max_ + 1)]
    for i, freq in t.items():
        bucket[freq].append(i)

    while k > 0 and bucket:
        top = bucket.pop()
        if not top:
            continue
        top.sort(reverse=True)
        while top and k > 0:
            print(top.pop(), end=' ')
            k -= 1


def main():
    input()
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    k = int(input())
    must_common(arr, k)


if __name__ == '__main__':
    main()