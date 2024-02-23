from queue import Queue

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
        graph[i].sort()
    return n, m, graph


def bfs(graph: list[list[int]], start_vertex: int, color: list):
    queue = Queue()
    queue.put(start_vertex - 1)
    while not queue.empty():
        vertex = queue.get()

        if color[vertex] == WHITE:
            print(vertex + 1, end=' ')
            color[vertex] = GRAY
            for w in graph[vertex]:
                if color[w - 1] == WHITE:
                    queue.put(w - 1)


def main():
    n, m, graph = input_graph()
    color = [WHITE for _ in range(n)]
    i = int(input())
    bfs(graph, i, color)


if __name__ == '__main__':
    main()
