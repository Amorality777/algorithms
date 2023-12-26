def merge(seq: list[list[int]]) -> list[list[int]]:
    if len(seq) <= 1:
        return seq

    return seq


def main():
    n = int(input())
    flower_beds = [list(map(int, input().split())) for _ in range(n)]
