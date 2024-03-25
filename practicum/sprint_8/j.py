import sys
from collections import defaultdict


class Trie:

    def __init__(self, is_word: bool = False):
        self.is_word = is_word
        self.children = {}

    def add_word(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.is_word = True

    def find_word(self, word: str):
        curr = self
        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        return curr

    def collect(self, cur_word) -> list:
        result = []
        if self.is_word:
            result.append(cur_word)
        for char, child in self.children.items():
            result.extend(child.collect(cur_word + char))
        return result


def main():
    data = defaultdict(list)

    root = Trie()
    for _ in range(int(input())):
        titles = ''
        word = ''
        for char in sys.stdin.readline().rstrip():
            if char == char.title():
                titles += char
            word += char
        data[titles].append(word)
        root.add_word(titles)

    for title in data.keys():
        data[title].sort(key=lambda word: word.lower())

    for _ in range(int(input())):
        titles = sys.stdin.readline().rstrip()
        curr = root.find_word(titles)
        if curr is None:
            continue
        res = []
        for key in curr.collect(titles):
            res.extend(data[key])
        print('\n'.join(sorted(res)))


main()
