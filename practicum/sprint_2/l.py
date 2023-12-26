def fibonacci(n: int, k: int) -> int:
    if n < 2:
        return 1
    double_prev = 1
    prev = 1

    for i in range(2, n + 1):
        s = (double_prev + prev) % 10 ** k
        double_prev, prev = prev, s
    return s


def main():
    n, k = input().split()

    print(fibonacci(int(n), int(k)))


main()
