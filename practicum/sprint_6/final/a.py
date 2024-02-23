"""
https://contest.yandex.ru/contest/25070/run-report/106882915/
-- ПРИНЦИП РАБОТЫ --
0. Чтение данных. Граф привожу к виду массива словарей,
где индекс массива - начальная вершина, ключ словаря - конечная вершина, значение - вес ребра.

Класс MaxSpanningTree:
1. Для хранения добавленных и не добавленных в остов вершин используются сеты.
2. Для хранения ребер используется куча
(переработанный в класс код из прошлого финального задания + компаратор по весу ребра)
формат хранения данных в куче - кортеж (вес ребра, начальная вершина, конечная вершина)
3. _extract_max - отдает ребро с максимальным весом из кучи
4. _add_vertex - перенос вершины в массив "добавленных" + удаление из "не добавленных",
добавление в кучу всех смежных вершин, которые еще не были добавлены в остов.

Алгоритм обхода:
0. В качестве начальной точки берется первая вершина и для нее вызывается _add_vertex (для инициирующего наполнения кучи).
1. Из кучи выбирается ребро с максимальным весом (за log(m))
2. Если конец ребра не был ранее добавлен в остов, то происходит вызов _add_vertex и увеличение "стоимости" сети.
3. Пункты 1-2 повторяются пока есть не добавленные вершины и ребра в обработке (в куче)

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции над сетами в алгоритме (вставка, удаление, вхождение) за О(1).
_extract_max - О(log(m)) извлечение из кучи.
_add_vertex - O(2*m*log(m)) - суммарно за весь скрипт, т.к. граф не ориентированный то *2
O(n*log(m) + 2*m*log(m)) => O((2m + n)*log(m)) - в худшем случае
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
added + not_added = O(n)
edges = О(m)
O(n + m)
"""
import sys


def input_graph() -> tuple[int, int, list[dict[int, int]]]:
    n, m = sys.stdin.readline().split()
    n, m = int(n), int(m)
    graph = [{} for _ in range(n)]
    for _ in range(m):
        u, v, w = sys.stdin.readline().split()
        if u == v:
            continue
        u, v, w = int(u) - 1, int(v) - 1, int(w)
        u, v = (u, v) if u <= v else (v, u)
        if (w_old := graph[u].get(v)) is not None:
            w = max(w_old, w)
        graph[u][v] = w
        graph[v][u] = w

    return n, m, graph


class Heap:
    def __init__(self):
        self.heap: list[tuple[int, int, int]] = [(-1, -1, -1)]

    def __bool__(self):
        return len(self.heap) > 1

    def _compare(self, left: int, right: int) -> bool:
        return self.heap[left][0] > self.heap[right][0]

    def _sift_up(self, idx):
        parent = idx // 2
        if parent >= 1 and self._compare(idx, parent):
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            self._sift_up(parent)

    def add(self, item: tuple[int, int, int]):
        index = len(self.heap)
        self.heap.append(item)
        self._sift_up(index)

    def _sift_down(self, index):
        left, right = 2 * index, 2 * index + 1

        if len(self.heap) <= left:
            return

        index_min = right if right < len(self.heap) and not self._compare(left, right) else left

        if not self._compare(index, index_min):
            self.heap[index], self.heap[index_min] = self.heap[index_min], self.heap[index]
            self._sift_down(index_min)

    def pop_max(self):
        result = self.heap[1]
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self._sift_down(1)
        return result


class MaxSpanningTree:
    def __init__(self, graph: list[dict[int, int]]):
        self.graph = graph
        self.added = set()
        self.not_added = set(range(len(self.graph)))
        self.edges = Heap()
        self.cost = 0

    def _extract_max(self) -> tuple[int, int, int]:
        return self.edges.pop_max()

    def _add_vertex(self, v: int) -> None:
        self.added.add(v)
        self.not_added.remove(v)
        for w in self.graph[v].keys():
            if w not in self.added:
                self.edges.add((self.graph[v][w], v, w))

    def run(self):
        self._add_vertex(0)

        while self.not_added and self.edges:
            _, u, v = self._extract_max()
            if v in self.not_added:
                self._add_vertex(v)
                self.cost += self.graph[u][v]


def main():
    n, m, graph = input_graph()
    obj = MaxSpanningTree(graph)
    obj.run()
    return 'Oops! I did it again' if obj.not_added else obj.cost


if __name__ == '__main__':
    print(main())
