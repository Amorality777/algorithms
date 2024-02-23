def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v)

    for v in graph:
        print(len(v), ' '.join(map(str, v)))


if __name__ == '__main__':
    main()
