"""
https://contest.yandex.ru/contest/26133/run-report/110445988/вш
-- ПРИНЦИП РАБОТЫ --
Все возможные слова будут храниться в префиксном дереве

Далее по принципу динамического программирования можно перебрать возможные варианты комбинаций слов.
 - Что будет храниться в массиве dp?
 dp[i] - будет хранится булево значение - можно ли до этого элемента разбить строку на валидные слова.

 - Каким будет базовый случай для задачи?
Если длина T равно нулю, то строку можно собрать - базовый случай.

 - Каким будет переход динамики?
Необходимо взять за "начало строки" i и для каждого возможного окончания слова j проставлять dp[j] = True
(Дополнительно учитывать сдвиг нулевого элемента)

 - Каким будет порядок вычисления данных в массиве dp?
Поэтапно перебирать все возможные начала строки i, если i-1=True (до предыдущего элемента строку можно разбить на слова),
то от i необходимо произвести переход

 - Где будет располагаться ответ на исходный вопрос?
В последнем элементе массива dp

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(L) - построение дерева, где L суммарная длина слов
О(Tl^2), где Tl - длина строки T
Итого: О(L + Tl^2)
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(L) - хранение дерева
О(Tl) - хранение массива dp
Итого: О(L + Tl)
"""
import sys


class Trie:

    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.is_word = True


def is_sentence(text: str, trie: Trie) -> bool:
    dp = [False] * (len(text) + 1)
    dp[0] = True
    for i in range(1, len(text) + 1):
        if dp[i - 1]:
            curr = trie
            for j in range(i - 1, len(text)):
                char = text[j]
                if char not in curr.children:
                    break
                curr = curr.children[char]
                if curr.is_word:
                    dp[j + 1] = True
            if dp[-1]:
                return True
    return dp[-1]


def main():
    t = sys.stdin.readline().rstrip()
    trie = Trie()
    for _ in range(int(input())):
        trie.add_word(sys.stdin.readline().rstrip())
    print("YES" if is_sentence(t, trie) else "NO")


main()
