import sys


def sum_fourth(seq: list[int], target: int) -> set:
    seq.sort()
    sums = set()
    l_s = len(seq)
    for i in range(0, l_s - 3):
        for j in range(i + 1, l_s - 2):
            k = target - seq[i] - seq[j]

            left = j + 1
            right = l_s - 1
            while left < right:
                if (res := seq[left] + seq[right]) > k:
                    right -= 1
                elif res < k:
                    left += 1
                else:
                    sums.add((seq[i], seq[j], seq[left], seq[right]))
                    left += 1
                    right -= 1

    return sums


def effective_solution(x, a):
    if not x:
        return set()
    x.sort()
    history = {x[0]}
    n = len(x)
    triples = set()
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                target = a - x[i] - x[j] - x[k]
                if target in history:
                    triples.add((target, x[i], x[j], x[k]))
        history.add(x[i])
    return triples


def main():
    input()
    target = int(input())
    seq = list(map(int, sys.stdin.readline().rstrip().split()))

    result = effective_solution(seq, target)
    print(len(result))
    for res in sorted(result):
        print(*res)


main()
