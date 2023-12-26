def sieve(n: int) -> list:
    lp = [0 for _ in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        curr = lp[i]
        for p in primes:
            x = i * p
            if x > n or p > curr:
                break
            lp[x] = p
    return primes
