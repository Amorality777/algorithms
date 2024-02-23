from collections import defaultdict

WHITE = 1
GRAY = 2
BLACK = 3


def input_graph() -> tuple[int, int, list[list[int]]]:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v)

    for i in range(n):
        graph[i].sort(reverse=True)
    return n, m, graph


def dfs(graph: list[list[int]], start_vertex: int, color: list, time: defaultdict):
    stack = [start_vertex - 1]
    now = 0
    while stack:
        vertex = stack.pop()

        if color[vertex] == WHITE:
            color[vertex] = GRAY
            stack.append(vertex)
            time[vertex].append(now)
            now += 1
            for w in graph[vertex]:
                if color[w - 1] == WHITE:
                    stack.append(w - 1)
        elif color[vertex] == GRAY:
            time[vertex].append(now)
            now += 1
            color[vertex] = BLACK


def main():
    n, m, graph = input_graph()
    color = [WHITE for _ in range(n)]
    time = defaultdict(list)
    dfs(graph, 1, color, time)
    for key in sorted(time):
        print(' '.join(map(str, time[key])))


if __name__ == '__main__':
    main()
