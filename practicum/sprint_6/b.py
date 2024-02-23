def main():
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        matrix[u - 1][v - 1] = 1

    for row in matrix:
        print(' '.join(map(str, row)))


if __name__ == '__main__':
    main()
