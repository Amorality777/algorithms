def fibonacci(n: int) -> int:
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(int(input())))
