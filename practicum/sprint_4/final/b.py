import sys


class HashTable:
    DELETED_KEY = 0

    def __init__(self, length: int):
        self.length = length
        self.table: list[tuple[int, str] | int | None] = [None] * self.length

    def _find_curr_bucket(self, key) -> [int | None]:
        bucket = self._get_bucket(key)
        curr = self.table[bucket]
        step = 1
        while True:
            if curr is None:
                return None
            elif curr == self.DELETED_KEY or curr[0] != key:
                bucket = self._get_next_bucket(bucket, step)
                step += 1
                curr = self.table[bucket]
                continue
            return bucket

    def _find_free_bucket(self, key) -> [int | None]:
        bucket = self._get_bucket(key)
        curr = self.table[bucket]
        step = 1
        while True:
            if curr is None or curr == self.DELETED_KEY:
                return bucket
            elif curr[0] != key:
                bucket = self._get_next_bucket(bucket, step)
                step += 1
                curr = self.table[bucket]
                continue
            return bucket

    def put(self, key: int, value: str) -> None:
        bucket = self._find_free_bucket(self._get_hash(key))
        self.table[bucket] = (key, value)

    def get(self, key: int) -> [None | str]:
        bucket = self._find_curr_bucket(self._get_hash(key))
        return self.table[bucket][1] if bucket is not None else None

    def delete(self, key: int) -> [None | str]:
        bucket = self._find_curr_bucket(self._get_hash(key))
        if bucket is None:
            return None
        value = self.table[bucket][1]
        self.table[bucket] = self.DELETED_KEY
        return value

    def _get_next_bucket(self, bucket: int, step) -> int:
        return (bucket + 53 * step + 13 * step * step) % self.length

    def _get_hash(self, key: int) -> int:
        return key

    def _get_bucket(self, hash_: int) -> int:
        return hash_ % self.length


def calc_table_len(commands_count: int) -> int:
    primes = [133417, 80039, 48023, 28813, 17257, 10343, 6203, 3719, 2221, 1327, 787, 467, 277, 163, 97, 31]
    max_inserts = int(min(100000, commands_count) * 1.3)
    prev = primes[0]
    for prime in primes:
        if max_inserts > prime:
            return prev
        prev = prime
    return prev


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
