#  https://contest.yandex.ru/contest/22450/run-report/98113731/
#  Время - О(2n-1) в худшем случае => с округлением O(n)
#  Дополнительная память - О(1)

def street_counter(s: list[int]) -> list[int]:
    last_empty = None
    nxt = 1
    for i in range(len(s)):
        if s[i] != 0:
            s[i] = nxt
            nxt += 1
        else:
            left_bord = -1 if last_empty is None else (last_empty + i) // 2
            for count, j in enumerate(range(i - 1, left_bord, -1), start=1):
                s[j] = count
            last_empty = i
            nxt = 1

    return s


def main():
    input()
    street = list(map(int, input().split()))

    print(*street_counter(street))


if __name__ == '__main__':
    main()
