import sys


def find_lcs(f: str, s: str) -> str:
    dp = [[0] * (len(s) + 1) for _ in range(len(f) + 1)]

    for i in range(1, len(f) + 1):
        for j in range(1, len(s) + 1):
            if f[i - 1] == s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return _restore_ans(f, s, dp)


def _restore_ans(f: str, s: str, dp: list[list[int]]) -> str:
    ans = []
    i = len(dp) - 1
    j = len(dp[0]) - 1
    while dp[i][j] != 0:
        if f[i - 1] == s[j - 1]:
            ans.append(f[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i][j - 1]:
                j -= 1
            else:
                i -= 1
    return ''.join(reversed(ans))


def main():
    first = sys.stdin.readline().strip()
    second = sys.stdin.readline().strip()
    first, second = (first, second) if len(first) >= len(second) else (second, first)

    dp = find_lcs(first, second)
    print(dp)


main()
