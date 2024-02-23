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
        u, v = int(u) - 1, int(v) - 1
        graph[u].append(v)
        graph[v].append(u)

    return n, m, graph


def bfs(graph: list[list[int]], start_vertex: int, colors: list, distance: list, end_v: int) -> int:
    if start_vertex == end_v:
        return 0
    queue = Queue()
    start_vertex = start_vertex
    queue.put(start_vertex)
    colors[start_vertex] = GRAY
    distance[start_vertex] = 0

    while not queue.empty():
        vertex = queue.get()

        for w in graph[vertex]:
            if w == end_v:
                return distance[vertex] + 1
            if colors[w] == WHITE:
                colors[w] = GRAY
                d = distance[vertex] + 1
                distance[w] = d

                queue.put(w)

        colors[vertex] = BLACK
    return -1


def main():
    n, m, graph = input_graph()
    colors = [WHITE for _ in range(n)]
    distance = [-1 for _ in range(n)]
    s, e = sys.stdin.readline().split()
    s, e = int(s) - 1, int(e) - 1
    print(bfs(graph, s, colors, distance, e))


if __name__ == '__main__':
    main()
