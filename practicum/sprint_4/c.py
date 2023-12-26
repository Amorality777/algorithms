import sys


def generate_a(a: int, m: int, seq_l: int) -> tuple:
    prepared = [0] * (seq_l + 1)
    prepared[0] = 1
    a_gen = 1
    for i in range(1, seq_l):
        a_gen = (a_gen * a) % m
        prepared[i] = a_gen

    return tuple(prepared)


def generate_hashes(a: int, m: int, seq: str) -> tuple:
    res = [0] * len(seq)
    prev = 0

    for i, char in enumerate(seq):
        res[i] = (prev * a + ord(char)) % m
        prev = res[i]

    return tuple(res)


def main():
    a = int(input())
    m = int(input())

    seq = sys.stdin.readline().rstrip()
    seq_hashes = generate_hashes(a, m, seq)
    a = generate_a(a, m, len(seq))

    for _ in range(int(input())):
        l, r = sys.stdin.readline().rstrip().split()
        l, r = int(l), int(r)
        left = seq_hashes[l - 2] if l - 2 >= 0 else 0
        print((seq_hashes[r - 1] - ((left * a[r - l + 1]) % m)) % m)


main()
