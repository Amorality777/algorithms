WHITE = 1
GRAY = 2
BLACK = 3


def input_graph() -> tuple[int, int, list[list[int]]]:
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(v)
        graph[v - 1].append(u)

    for i in range(n):
        graph[i].sort(reverse=True)
    return n, m, graph


def dfs(graph: list[list[int]], start_vertex: int, color: list):
    stack = [start_vertex - 1]

    while stack:
        vertex = stack.pop()

        if color[vertex] == WHITE:
            print(vertex + 1, end=' ')
            color[vertex] = GRAY
            stack.append(vertex)
            for w in graph[vertex]:
                if color[w - 1] == WHITE:
                    stack.append(w - 1)
        elif color[vertex] == GRAY:
            color[vertex] = BLACK


def main():
    n, m, graph = input_graph()
    color = [WHITE for _ in range(n)]
    i = int(input())
    dfs(graph, i, color)


if __name__ == '__main__':
    main()
