import sys
from queue import Queue

WHITE = 1
GRAY = 2
BLACK = 3


def input_graph() -> tuple[int, int, list[list[int]]]:
    n, m = sys.stdin.readline().split()
    n, m = int(n), int(m)
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = sys.stdin.readline().split()
        u, v = int(u), int(v)
        graph[u - 1].append(v)
        graph[v - 1].append(u)

    for i in range(n):
        graph[i].sort()
    return n, m, graph


def bfs(graph: list[list[int]], start_vertex: int, colors: list, distance: list) -> int:
    queue = Queue()
    start_vertex = start_vertex - 1
    queue.put(start_vertex)
    colors[start_vertex] = GRAY
    distance[start_vertex] = 0
    max_ = 0
    while not queue.empty():
        vertex = queue.get()

        for w in graph[vertex]:
            w = w - 1
            if colors[w] == WHITE:
                colors[w] = GRAY
                d = distance[vertex] + 1
                distance[w] = d
                max_ = max(max_, d)
                queue.put(w)

        colors[vertex] = BLACK
    return max_


def main():
    n, m, graph = input_graph()
    colors = [WHITE for _ in range(n)]
    distance = [-1 for _ in range(n)]
    s = int(input())

    print(bfs(graph, s, colors, distance))


if __name__ == '__main__':
    main()
