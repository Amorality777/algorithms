"""
https://contest.yandex.ru/contest/23815/run-report/102242208/
-- ПРИНЦИП РАБОТЫ --
Алгоритм реализован на основе бинарного поиска.
Отличием является определение "не поломанной" половины.
Т.е. можно утверждать, что одна из половин начального массива будет корректно отсортирована (без разрыва) =>
по этой стороне можно определить принадлежит ли целевой элемент корректной половине массива,
если да, то продолжаем поиск в этой половине массива, иначе в другой.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
О(log(n))

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(log(n)) - вычисляется по максимально возможному уровню стека.
"""


def broken_search(nums, target) -> int:
    if (count := len(nums)) == 0:
        return -1
    mid = count // 2
    if nums[mid] == target:
        return mid
    if nums[0] < nums[mid]:
        go_left = nums[0] <= target < nums[mid]
    else:
        go_left = not nums[-1] >= target > nums[mid]

    if go_left:
        return broken_search(nums[0: mid], target)
    else:
        res = broken_search(nums[mid + 1:], target)
        return res + mid + 1 if res != -1 else res
