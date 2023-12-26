# Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
#
# Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.


def read_input() -> tuple[list, int, int, int, int]:
    c = int(input())
    r = int(input())
    matrix = []
    for i in range(c):
        matrix.append(list(map(int, input().split())))
    x, y = int(input()), int(input())
    return matrix, x, y, c, r


def is_valid(target: int, len_: int) -> bool:
    return len_ > target >= 0


def neighbours_count(matrix: list[list], x: int, y: int, col: int, row: int) -> list[int]:
    n = []
    points = (
        (x, y + 1),
        (x, y - 1),
        (x + 1, y),
        (x - 1, y)
    )
    for x_exp, y_exp in points:
        if is_valid(x_exp, col) and is_valid(y_exp, row):
            n.append(matrix[x_exp][y_exp])
    n.sort()
    return n


if __name__ == '__main__':
    result = neighbours_count(*read_input())
    print(' '.join(map(str, result)))
