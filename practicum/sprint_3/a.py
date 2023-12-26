def combine(n: int, seq: str, left: int, right: int):
    if left == n and right == n:
        print(seq)
        return
    if left < n:
        combine(n, seq + '(', left + 1, right)
    if right < left:
        combine(n, seq + ')', left, right + 1)


combine(int(input()), '', 0, 0)
