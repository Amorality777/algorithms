from sys import stdin


def max_triangle_per(sides: list[int]) -> int:
    sides.sort(reverse=True)
    for i in range(2, len(sides)):
        if sides[i] + sides[i - 1] > sides[i - 2]:
            return sides[i] + sides[i - 1] + sides[i - 2]

    return -1


def main():
    input()
    sides = list(map(int, stdin.readline().rstrip().split()))

    print(max_triangle_per(sides))


if __name__ == '__main__':
    main()
