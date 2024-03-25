import sys


def find(seq: tuple, pattern: tuple, start: int) -> int:
    if len(seq) < len(pattern):
        return -1
    for pos in range(start, len(seq) - len(pattern) + 1):
        match = True
        const = seq[pos]
        for offset in range(len(pattern)):
            if seq[pos + offset] - const != pattern[offset]:
                match = False
                break
        if match:
            return pos
    return -1


def find_all(seq: tuple, pattern: tuple) -> list:
    occurrences = []
    start = 0
    while True:
        pos = find(seq, pattern, start)
        if pos == -1:
            break
        start = pos + 1
        occurrences.append(pos + 1)

    return occurrences


def prepare_pattern(seq: map) -> tuple:
    first = next(seq)
    return 0, *tuple(i - first for i in seq)


def main():
    input()
    s = tuple(map(int, sys.stdin.readline().rstrip().split()))
    input()
    pattern = prepare_pattern(map(int, sys.stdin.readline().rstrip().split()))
    print(*find_all(s, pattern))


main()
