def insert_sort(a: list) -> None:
    """Сортировка вставками.

    Args:
        a (list): список для сортировки.
    """
    for j in range(1, len(a)):
        tmp = a[j]
        while j > 0 and tmp < a[j - 1]:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
