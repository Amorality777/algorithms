"""
https://contest.yandex.ru/contest/24810/run-report/105463600/
-- ПРИНЦИП РАБОТЫ --
1. Заполнение пирамиды приоритета от минимального к максимальному.
heap_add добавляет в конец кучи новое значение, далее sift_up просеивает значение вверх до баланса.
2. Удаление верхнего элемента из кучи (наименьшего) и формирование отсортированного массива
pop_min берет первый элемент из кучи, на его место ставится последний элемент кучи и он просеивается вниз до баланса.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(n*log n)
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
O(n)
"""
import sys


def sift_up(heap, idx):
    parent = idx // 2
    if parent >= 1 and heap[idx] < heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        sift_up(heap, parent)


def heap_add(heap, item):
    index = len(heap)
    heap.append(item)
    sift_up(heap, index)


def sift_down(heap, index):
    left, right = 2 * index, 2 * index + 1

    if len(heap) <= left:
        return

    index_min = right if right < len(heap) and heap[left] > heap[right] else left

    if heap[index] > heap[index_min]:
        heap[index], heap[index_min] = heap[index_min], heap[index]
        sift_down(heap, index_min)


def pop_min(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result


def heap_sort(array: list):
    heap = [-1]

    for item in array:
        heap_add(heap, item)

    sortedArray = []
    while len(heap) > 1:
        max_val = pop_min(heap)
        sortedArray.append(max_val)

    return sortedArray


def main():
    n = int(input())
    players = []
    for _ in range(n):
        name, wins, tries = sys.stdin.readline().rstrip().split()
        players.append((-int(wins), int(tries), name))

    players = heap_sort(players)
    print('\n'.join((player[2] for player in players)))


if __name__ == "__main__":
    main()
