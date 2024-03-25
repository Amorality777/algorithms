import sys


def solution(seq: tuple, exp: int) -> int:
    curr = [float('inf') for _ in range(1, exp + 1)]

    for i in range(1, exp + 1):
        prev = curr[:]


def main():
    exp = int(input())
    input()
    denoms = tuple(set(map(int, sys.stdin.readline().rstrip().split())))
    print(solution(denoms, exp))
