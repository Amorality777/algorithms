"""
https://contest.yandex.ru/contest/25070/run-report/106958630/
-- ПРИНЦИП РАБОТЫ --
Если дорогу типа R воспринимать как "обратную",
то модель железных дорог можно представить как направленный граф,
а условие, что есть 2 дороги из одного города как наличие цикла в графе.

Сам алгоритм поиска циклов основан на обходе в глубину,
если для очередной "новой" вершины будет найдена соседняя вершина,
которая находится в обработке (серая), то есть цикл и карта не оптимальна.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
кол-во ребер v = n*(n-1)/2
О(v+n) -> О(n(1/2 + n/2)) -> ~O(n*n)
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
colors = O(n)
stack = O(v)
О(v+n) -> ~O(n*n)
"""
WHITE = 1
GRAY = 2
BLACK = 3


def input_graph() -> tuple[int, list[list[int]]]:
    n = int(input())
    graph = [[] for _ in range(n)]
    for i in range(1, n):
        for j, char in enumerate(input(), start=1):
            u, v = (i, i + j) if char == 'B' else (i + j, i)
            graph[u - 1].append(v - 1)

    return n, graph


def has_cycle(graph: list[list[int]], start_vertex: int, colors: list[int]) -> bool:
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if colors[vertex] == GRAY:
            colors[vertex] = BLACK
        elif colors[vertex] == WHITE:
            colors[vertex] = GRAY
            stack.append(vertex)
            for w in graph[vertex]:
                if colors[w] == GRAY:
                    return True
                elif colors[w] == WHITE:
                    stack.append(w)
    return False


def main():
    n, graph = input_graph()
    colors = [WHITE for _ in range(len(graph))]
    has_c = False
    for i in range(len(colors)):
        if colors[i] == WHITE:
            has_c = has_cycle(graph, i, colors)
            if has_c:
                break
    print('NO' if has_c else 'YES')


if __name__ == '__main__':
    main()
