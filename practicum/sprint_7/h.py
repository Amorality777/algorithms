def get_input() -> tuple[int, int, list[list[int]]]:
    n, m = map(int, input().split())
    return n, m, [list(map(int, input())) for _ in range(n)]


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


def main():
    n, m, field = get_input()
    print(solve(n, m, field))


main()
