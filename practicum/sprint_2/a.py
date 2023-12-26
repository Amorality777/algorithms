import sys
from time import time


def get_input() -> tuple:
    n = int(input())
    m = int(input())

    matrix = [sys.stdin.readline().rstrip().split() for _ in range(n)]

    return matrix, n, m


def matrix_transpon(matrix: list[list[str]], n: int, m: int) -> str:
    result = [['' for _ in range(n)] for _ in range(m)]
    for j in range(m):
        for i in range(n):
            result[j][i] = matrix[i][j]

    return '\n'.join((' '.join(rows) for rows in result))


start = time()
print(matrix_transpon(*get_input()))

print(time() - start)
