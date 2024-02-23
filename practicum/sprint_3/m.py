import sys


def mediate(left: list, right: list, l_size: int, r_size: int, k: int) -> tuple[list, list, int, int, float]:
    if l_size > r_size:
        return mediate(right, left, r_size, l_size, k)

    if l_size == 0:
        return right[k - 1]

    if k == 1:
        l = len(left) - l_size
        r = len(right) - r_size
        if left[l] > right[r]:
            r_size += 1
        else:
            l_size += 1
        return left, right, l_size, r_size, min(left[l], right[r])

    half_k = k // 2
    i = min(l_size, half_k)
    j = min(r_size, half_k)
    if left[i - 1] < right[j - 1]:
        return mediate(left, right, l_size - i, r_size, k - i)
    else:
        return mediate(left, right, l_size, r_size - j, k - j)


def main():
    l = int(input())
    r = int(input())
    left = list(map(int, sys.stdin.readline().rstrip().split()))
    right = list(map(int, sys.stdin.readline().rstrip().split()))
    get_double = (l + r) % 2 == 0
    k = (l + r + 1) // 2
    left, right, l_size, r_size, res = mediate(left, right, l, r, k)
    if get_double:
        res += mediate(left, right, l_size, r_size, 1)[-1]
        res /= 2
    print(res)


if __name__ == '__main__':
    main()
