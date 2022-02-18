def sieve_of_eratosthenes(n: int) -> dict:
    """Решето́ Эратосфе́на — алгоритм нахождения всех простых чисел до целого числа n.

    Args:
        n (int): Длина проверки списка.

    Returns:
        dict: Ключи - числа от 2, до n, значение - True, если число простое, иначе False.
    """
    sieve = {value: True for value in range(2, n)}
    for key, value in sieve.items():
        if not value:
            continue
        for m in range(2 * key, n, key):
            sieve[m] = False
    return sieve


