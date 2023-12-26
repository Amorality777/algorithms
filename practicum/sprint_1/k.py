def bring_to_one_len(s: str | list, current_len: int) -> str | list:
    if isinstance(s, str):
        return f"{s:>0{current_len}}"
    if len(s) >= current_len:
        return s
    l = current_len - len(s)
    return ['0'] * l + s


def _sum(f: list, s: str, f_l) -> reversed:
    f = bring_to_one_len(f, len(s))
    s = bring_to_one_len(s, f_l)

    result = []
    prev = 0
    for i in range(len(f) - 1, -1, -1):
        curr_sum = int(f[i]) + int(s[i]) + prev
        prev = 0
        if curr_sum > 9:
            prev = 1
            curr_sum -= 10
        result.append(curr_sum)

    if prev:
        result.append(prev)
    return reversed(result)


def main():
    n_count = input()
    n = input().split()
    k = input()
    print(*_sum(n, k, n_count))


if __name__ == '__main__':
    main()
