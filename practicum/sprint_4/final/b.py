"""
https://contest.yandex.ru/contest/24414/run-report/103981019/
-- ПРИНЦИП РАБОТЫ --
Получение длины таблицы:
Берем минимальное из ожидаемого кол-ва команд и ограничения задачи, умножаем на коэффициент +30%,
далее берем ближайшее простое число из заранее вычисленных констант (между простыми числами тоже шаг ~ +30%).

Особенности хеш таблицы:
В качестве хеш функции просто возвращается ключ (т.к. ключ - число),
вычисление корзины производится получением остатка от длины таблицы.

Решение коллизий:
Методом открытой адресации, квадратичным пробированием с коэф 53, 13 (не участвуют в выборе длины таблицы).

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Т.к. длины и коэффициенты шагов - взаимно простые числа, то среднее выполнение команды за О(1), в худшем случае О(n).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(n) - если все операции на вставку.
"""
import sys


class HashTable:
    EMPTY_KEY = 1
    DELETED_KEY = 0

    STEP_ODDS = 53
    STEP_SQR_ODDS = 13

    def __init__(self, length: int):
        self.length = length
        self.data: list[tuple[int, str] | int] = [self.EMPTY_KEY] * self.length

    def _find_curr_bucket(self, key: int) -> [int | None]:
        bucket = self._get_bucket(self._get_hash(key))
        curr = self.data[bucket]
        step = 1
        while True:
            if curr == self.EMPTY_KEY:
                return None
            elif curr == self.DELETED_KEY or curr[0] != key:
                bucket = self._get_next_bucket(bucket, step)
                step += 1
                curr = self.data[bucket]
                continue
            return bucket

    def _find_free_bucket(self, key: int) -> [int | None]:
        bucket = self._get_bucket(self._get_hash(key))
        curr = self.data[bucket]
        step = 1
        while True:
            if curr in (self.EMPTY_KEY, self.DELETED_KEY):
                return bucket
            elif curr[0] != key:
                bucket = self._get_next_bucket(bucket, step)
                step += 1
                curr = self.data[bucket]
                continue
            return bucket

    def put(self, key: int, value: str) -> None:
        bucket = self._find_free_bucket(key)
        self.data[bucket] = (key, value)

    def get(self, key: int) -> [None | str]:
        bucket = self._find_curr_bucket(key)
        return self.data[bucket][1] if bucket is not None else None

    def delete(self, key: int) -> [None | str]:
        bucket = self._find_curr_bucket(key)
        if bucket is None:
            return None
        value = self.data[bucket][1]
        self.data[bucket] = self.DELETED_KEY
        return value

    def _get_next_bucket(self, bucket: int, step) -> int:
        return (bucket + self.STEP_ODDS * step + self.STEP_SQR_ODDS * step * step) % self.length

    def _get_hash(self, key: int) -> int:
        return key

    def _get_bucket(self, hash_: int) -> int:
        return hash_ % self.length


def calc_table_len(commands_count: int) -> int:
    COEF = 1.3
    PRIMES = [133417, 80039, 48023, 28813, 17257, 10343, 6203, 3719, 2221, 1327, 787, 467, 277, 163, 97, 31]
    max_inserts = int(min(100000, commands_count) * COEF)
    for i in range(1, len(PRIMES)):
        if max_inserts > PRIMES[i]:
            return PRIMES[i - 1]
    return PRIMES[-1]


def main():
    n = int(input())
    table = HashTable(calc_table_len(n))
    for _ in range(n):
        command = sys.stdin.readline().rstrip()
        if command.startswith('put'):
            command, key, value = command.split()
            getattr(table, command)(int(key), value)
        else:
            command, key = command.split()
            print(getattr(table, command)(int(key)))


main()
