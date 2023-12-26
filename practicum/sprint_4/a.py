import sys


def hash_(seq: str, a: int, m: int) -> int:
    sum_ = 0
    a_gen = 1
    for i in range(len(seq) - 1, -1, -1):
        sum_ += (a_gen * ord(seq[i])) % m
        a_gen = (a_gen * a) % m
    return sum_ % m


def main():
    a = int(input())
    m = int(input())
    seq = sys.stdin.readline().rstrip()
    print(hash_(seq, a, m))
main()