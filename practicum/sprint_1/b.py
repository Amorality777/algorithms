#  https://contest.yandex.ru/contest/22450/run-report/98114841/
#  Время - О(10n), где n - кол-во кнопок (в данном случае 16) => с округлением O(n)
#  Дополнительная память - О(1), словарь с не более чем 10-ю записями.
from collections import defaultdict


def get_input() -> tuple:
    k = int(input())

    rows = [input() for _ in range(4)]

    return rows, k


def prepare_rows(rows: list[str]) -> dict:
    data = defaultdict(int)
    for row in rows:
        for char in row:
            if char.isdigit():
                data[int(char)] += 1

    return data


def score(rows: list[str], k: int) -> int:
    k *= 2
    data = prepare_rows(rows)

    return sum(k >= value for value in data.values())


print(score(*get_input()))
