def compare(left: str, right: str) -> bool:
    return left + right < right + left


# 783 1 2
# 783
# -1
def insertion_sort(seq: list, less) -> list:
    for i in range(1, len(seq)):
        item = seq[i]
        j = i - 1
        while j >= 0 and less(seq[j], item):
            seq[j + 1] = seq[j]
            j -= 1
        seq[j + 1] = item
    return seq


input()
print(''.join(insertion_sort(input().split(), compare)))
