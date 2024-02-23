M = 1000000007


def stairs_game(n: int, k: int) -> int:  # 5, 5
    if n == 1:
        return 1
    steps = [0] * max((n - 1), k)  # [1, 2, 4, 8]
    steps[0] = 1
    sum_ = 1  # 15

    for i in range(1, k):  # 4
        s = (sum_ + 1) % M  # 8
        steps[i] = s
        sum_ = (sum_ + s) % M

    for i in range(k, n - 1):  # 4
        steps[i] = sum_
        sum_ = (2 * sum_ - steps[i - k]) % M

    return steps[n - 2]


n, k = list(map(int, input().split()))
print(stairs_game(n, k))
