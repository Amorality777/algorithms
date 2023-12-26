import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def sieve(n) -> list[str]:
    result = []
    sqrt = math.ceil(math.sqrt(n))
    lp = [0 for _ in range(sqrt + 1)]
    primes = []
    i = 2
    while i * i <= n:
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            while n % i == 0:
                result.append(str(i))
                n = n // i
                sqrt = math.ceil(math.sqrt(n))
            if n <= 1:
                return result

        curr = lp[i]
        for p in primes:
            x = p * curr
            if (p > curr) or (x > sqrt):
                break
            lp[x] = p
        i += 1
    if n:
        result.append(str(n))
    print(primes)
    return result


num = int(input())
print(sieve(num))
