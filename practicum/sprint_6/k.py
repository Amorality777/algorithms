class ShortPathSearch:
    def __init__(self, graph_matrix: list[list[int]]) -> None:
        self.graph_matrix = graph_matrix
        self.result = []
        self.visited = []
        self.distance = []

    def _setup(self):
        count = len(self.result)
        self.visited = [False] * len(self.graph_matrix)
        self.distance = [float('inf')] * len(self.graph_matrix)
        self.distance[count] = 0

    def _relax(self, u: int, v: int) -> None:
        """Выбор наименьшего расстояния."""
        d = self.distance[u] + self.graph_matrix[u][v]
        if self.distance[v] > d:
            self.distance[v] = d

    def _get_min_dist_not_visited_vertex(self) -> int:
        vertex = -1
        dist = float('inf')
        for v in range(len(self.visited)):
            if not self.visited[v] and self.distance[v] < dist:
                dist = self.distance[v]
                vertex = v
        return vertex

    def outgoing_edges(self, u) -> list[int]:
        """Получение смежных вершин."""
        return [i for i, v in enumerate(self.graph_matrix[u]) if v != 0]

    def run(self) -> list[list[int]]:
        for i in range(len(self.graph_matrix)):
            self._setup()
            if i == len(self.graph_matrix):
                break
            while True:
                u = self._get_min_dist_not_visited_vertex()
                if u == -1:
                    break
                self.visited[u] = True
                for v in self.outgoing_edges(u):
                    self._relax(u, v)
            self.result.append([v if v != float('inf') else -1 for v in self.distance])

        return self.result


def input_graph() -> list[list[int]]:
    n, m = map(int, input().split())
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        if matrix[u - 1][v - 1]:
            w = min(w, matrix[u - 1][v - 1])
        matrix[u - 1][v - 1] = w
        matrix[v - 1][u - 1] = w
    return matrix


def main():
    graph = input_graph()
    result = ShortPathSearch(graph).run()
    for row in result:
        print(*row)


if __name__ == '__main__':
    main()
