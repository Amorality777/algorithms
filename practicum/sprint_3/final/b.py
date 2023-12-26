"""
https://contest.yandex.ru/contest/23815/run-report/102242088/
-- ПРИНЦИП РАБОТЫ --
Подготовка данных:
    Чтоб избежать дополнительного прохода по элементам данные преобразуются при считывании.
    На первое место ставится число побед со знаком минус, на второе число попыток и последним остается логин.
    Данный способ расстановки данных позволяет использовать стандартные средства сравнения.
    В результате ожидается, что на первое место ("минимальное" значение) встанет победитель
    и т.д. по убыванию призовых мест и возрастанию значений массива.
Точка входа quick_sort:
    - отдает сортировку частей массива функции partition;
    - вызывает себя дважды на элементы левее и правее pivot;
    - если правая часть становится больше или равной левой, то рекурсия прекращается;
Функция partition:
    - получает pivot - элемент для сравнения остальной части массива;
    - pivot кладется слева (чтобы точно знать где он);
    - по двум указателям справа и слева сканируется массив,
    если одновременно слева элемент больше и справа меньше pivot, то они меняются местами;
    - Если указатели встретились (или пересеклись) предыдущий пункт прекращается;
    - pivot возвращается на место правого указателя (не левого, т.к. левый на конце может указывать на больший элемент);
    - функция возвращает индекс расположения pivot;
Функция get_pivot:
    - берет три элемента: первый, средний и последний;
    - возвращает индекс элемента, который не превосходит два других.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
О(n**2) - в худшем случае, в среднем работает за О(n*log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(n) в худшем случае - на хранение стека, если все элементы равны и pivot будет делить массив не пропорционально.
По условиям задачи элементы не повторяются, но пространственная оценка будет стремиться к О(n).
В среднем случае  О(log(n)) - так же на стек.
"""
import sys


def get_pivot(seq: list, left: int, right: int) -> int:
    if right - left < 2:
        return left if seq[left] <= seq[right] else right
    lf = seq[left]
    rg = seq[right]
    mid = (right - left) // 2
    if seq[mid] < lf < rg or rg < lf < seq[mid]:
        return left
    elif lf < seq[mid] < rg or rg < seq[mid] < lf:
        return mid
    else:
        return right


def partition(seq: list, left: int, right: int) -> int:
    pivot = get_pivot(seq, left, right)
    seq[left], seq[pivot] = seq[pivot], seq[left]
    pivot = left
    left += 1

    while right >= left:
        if seq[left] <= seq[pivot]:
            left += 1
        elif seq[right] > seq[pivot]:
            right -= 1
        else:
            seq[right], seq[left] = seq[left], seq[right]
            right -= 1
            left += 1

    seq[pivot], seq[right] = seq[right], seq[pivot]
    return right


def quick_sort(seq: list, left: int, right: int):
    if left >= right:
        return

    pivot = partition(seq, left, right)

    quick_sort(seq, left, pivot - 1)
    quick_sort(seq, pivot + 1, right)


def main():
    n = int(input())
    players = []

    for _ in range(n):
        name, wins, tries = sys.stdin.readline().rstrip().split()
        players.append((-int(wins), int(tries), name))
    quick_sort(players, 0, len(players) - 1)
    print('\n'.join((player[2] for player in players)))


if __name__ == '__main__':
    main()
