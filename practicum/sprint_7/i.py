import sys


def get_input() -> tuple[int, int, list[list[int]]]:
    n, m = map(int, input().split())
    return n, m, [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]


def solve(n: int, m: int, field: list[list[int]]) -> int:
    n -= 1
    for row in range(n, -1, -1):
        for col in range(m):
            points = 0
            if row < n:
                points = field[row + 1][col]
            if col > 0:
                points = max(points, field[row][col - 1])
            field[row][col] += points
    return field[0][m - 1]


def get_path(n: int, m: int, field: list[list[int]]) -> str:
    l = n + m - 2
    p = [None] * l

    row = 0
    col = m - 1
    n -= 1
    while l > 0:
        l -= 1
        if row == n:
            p[l] = 'R'
            col -= 1
            continue
        if col == 0:
            p[l] = 'U'
            row += 1
            continue
        step = 'R' if field[row][col - 1] >= field[row + 1][col] else 'U'
        p[l] = step
        if step == 'U':
            row += 1
        else:
            col -= 1

    return ''.join(p)


def main():
    n, m, field = get_input()
    print(solve(n, m, field))
    print(get_path(n, m, field))


main()
