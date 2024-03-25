def compare_with_equals_len(f, s, fails=1) -> bool:
    for i in range(len(f)):
        if f[i] != s[i]:
            fails -= 1
        if fails < 0:
            return False
    return True


def main() -> bool:
    f = input()
    s = input()

    if len(f) == len(s):
        return compare_with_equals_len(f, s)
    else:
        f, s = (f, s) if len(f) > len(s) else (s, f)
        for i in range(len(s)):
            if f[i] != s[i]:
                return compare_with_equals_len(f[i + 1:], s[i:], 0)
        return True


print('OK' if main() else 'FAIL')
