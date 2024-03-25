import sys


def get_input() -> tuple[int, list]:
    _, n = input().split()
    return int(n), list(map(int, sys.stdin.readline().rstrip().split()))


def get_max(n: int, weights: list) -> int:
    dp = [[0] * (n + 1) for _ in range(len(weights))]

    for i in range(len(weights)):
        curr_weight = weights[i]
        for j in range(1, n + 1):
            second = curr_weight + dp[i - 1][j - curr_weight] if j - curr_weight >= 0 else 0
            if second > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], second)

    return dp[-1][-1]


def main():
    n, golds = get_input()
    print(get_max(n, golds))


main()
