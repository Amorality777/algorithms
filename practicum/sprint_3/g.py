from sys import stdin


def sort_countable(colors: list[int]) -> list:
    count = [0, 0, 0]
    for value in colors:
        count[value] += 1

    result = []
    for i, value in enumerate(count):
        result += [i] * value
    return result


def main():
    input()
    colors = list(map(int, stdin.readline().rstrip().split()))

    print(*sort_countable(colors))


if __name__ == '__main__':
    main()
