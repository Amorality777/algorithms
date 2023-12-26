import sys
from collections import defaultdict


class Library:
    LIMIT = 5

    def __init__(self):
        self.count = 0
        self.indexes = {}

    def add_doc(self, sentence: str) -> None:
        self.count += 1
        data = {}
        for word in sentence.split():
            if word not in data:
                data[word] = 1
            else:
                data[word] += 1
        for word, count in data.items():
            if word in self.indexes:
                self.indexes[word].append((self.count, count))
            else:
                self.indexes[word] = [(self.count, count)]

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
