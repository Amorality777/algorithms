from math import factorial


def find_threes(n: int) -> int:
    return factorial(2 * n) // (factorial(n) * factorial(n + 1))


if __name__ == '__main__':
    n = int(input())
    print(find_threes(n))
