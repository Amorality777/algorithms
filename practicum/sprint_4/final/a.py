"""
https://contest.yandex.ru/contest/24414/run-report/103927663/
-- ПРИНЦИП РАБОТЫ --
1. Индексация документов:
Создается общая хеш таблица, где ключом является уникальное слово,
а значением список с id документа и кол-вом повторений слова в документе.
Метод add_doc добавляет в индекс очередной документ.
2. Поиск релевантных документов.
Для каждого уникального слова в поисковом запросе происходит получение списка документов (id, count).
Далее для каждого документа из списка по id идет суммирование "баллов",
в итоге получается общий список релевантных документов.

Список приводится к удобному для сортировки виду и возвращаются 5 id документов с наивысшим суммарным баллом.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление документа в общий индекс О(2k), где k - кол-во слов в строке/документе.
Т.е. добавление всех документов ~ О(n*k), где k - среднее значение кол-ва слов.

Поиск совпадений О(m*n + n + n*log(n)), где
 - первая часть перебор всех релевантных документов к каждому слову;
 - вторая преобразование перед сортировкой (в целом здесь можно подумать об оптимизации)
 - третья - сортировка;
Т.е. в худшем случае О(n*(m + log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для хранения индекса О(n*k), где k - среднее значение кол-ва слов.
Для поиска - О(n) - по кол-ву документов в индексе.
"""
import sys
from collections import defaultdict


class Library:
    LIMIT = 5

    def __init__(self):
        self.count_docs = 0
        self.indexes = {}

    def add_doc(self, sentence: str) -> None:
        self.count_docs += 1
        data = {}
        for word in sentence.split():
            if word not in data:
                data[word] = 1
            else:
                data[word] += 1
        for word, count in data.items():
            if word not in self.indexes:
                self.indexes[word] = []
            self.indexes[word].append((self.count_docs, count))

    def find_match(self, kwargs: set) -> list:
        match = defaultdict(int)
        for word in kwargs:
            docs = self.indexes.get(word, [])
            for idx, count in docs:
                match[idx] += count
        match = [(-count, idx) for idx, count in match.items()]
        match.sort()
        return [v[1] for v in match[:self.LIMIT]]


def main():
    library = Library()
    for _ in range(int(input())):
        library.add_doc(sys.stdin.readline().rstrip())

    for _ in range(int(input())):
        if res := library.find_match(set(sys.stdin.readline().rstrip().split())):
            print(*res)


main()
