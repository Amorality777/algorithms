def merge(arr, lf, mid, rg) -> list:
    i, j = lf, mid
    result = []
    while i < mid and j < rg:
        left = arr[i]
        right = arr[j]
        if right < left:
            result.append(right)
            j += 1
        else:
            result.append(left)
            i += 1
    while j < rg:
        result.append(arr[j])
        j += 1
    while i < mid:
        result.append(arr[i])
        i += 1
    return result


def merge_sort(arr, lf, rg):
    if rg - lf == 1:
        return
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    i = lf
    for value in merge(arr, lf, mid, rg):
        arr[i] = value
        i += 1


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected, b
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
