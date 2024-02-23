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


def bfs(graph: list[list[int]], start_vertex: int, colors: list) -> bool:
    curr = set()
    next_ = set()

    def setup_sets(el: int):
        nonlocal curr
        nonlocal next_
        if el in curr:
            return
        curr, next_ = next_, curr

    queue = Queue()
    start_vertex = start_vertex
    queue.put(start_vertex)
    colors[start_vertex] = GRAY
    curr.add(start_vertex)

    while not queue.empty():
        vertex = queue.get()
        setup_sets(vertex)

        for w in graph[vertex]:
            if w in curr:
                return False
            next_.add(w)
            if colors[w] == WHITE:
                colors[w] = GRAY
                queue.put(w)
        colors[vertex] = BLACK
    return True


def main():
    n, m, graph = input_graph()
    colors = [WHITE for _ in range(n)]
    res = True
    for i in range(len(colors)):
        if colors[i] == WHITE:
            res = res and bfs(graph, i, colors)
            if not res:
                break
    print('YES' if res else 'NO')


if __name__ == '__main__':
    main()
