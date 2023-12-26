def sieve_of_eratosthenes(n: int) -> list:
    """
    Решето́ Эратосфе́на — алгоритм нахождения всех простых чисел до целого числа n.

    Args:
        n: Длина проверки списка.
    """
    sieve = [value for value in range(n + 1)]
    sieve[0] = sieve[1] = False
    for value in range(2, n):
        if not value:
            continue
        for m in range(value * value, n + 1, value):
            sieve[m] = False
    return sieve


def get_least_primes_linear(n: int) -> list:
    """Нахождение простых чисел за О(n)."""
    primes = []  # Простые
    least_primes = [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        if least_primes[i] == 0:
            least_primes[i] = i
            primes.append(i)
        for p in primes:
            x = i * p
            if p > least_primes[i]:
                print('here', i, p, x, n, 'h')
                break
            if x > n:
                print('!!!!!!!!!', i, p, x, n, '!!!!!!!!!!!!!!!')
                break
            least_primes[x] = p
    return primes


get_least_primes_linear(100)
