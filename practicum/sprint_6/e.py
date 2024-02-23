from collections import defaultdict


def input_graph() -> tuple[int, int, list[list[int]]]:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v)
        graph[v - 1].append(u)

    for i in range(n):
        graph[i].sort()
    return n, m, graph


def bfs(graph: list[list[int]], start_vertex: int, colors: list, color: int):
    stack = [start_vertex - 1]

    while stack:
        vertex = stack.pop()

        if colors[vertex] == -1:
            colors[vertex] = color
            for w in graph[vertex]:
                if colors[w - 1] == -1:
                    stack.append(w - 1)


def main():
    n, m, graph = input_graph()
    colors = [-1 for _ in range(n)]
    color = 0
    for i in range(len(colors)):
        if colors[i] == -1:
            color += 1
            bfs(graph, i + 1, colors, color)
    print(color)
    d = defaultdict(list)
    for i in range(len(colors)):
        d[colors[i]].append(i + 1)
    for key in sorted(d):
        print(*d[key])


if __name__ == '__main__':
    main()
