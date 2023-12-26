def insert_sort(a: list) -> None:
    """Сортировка вставками.

    Args:
        a (list): список для сортировки.
    """
    for i in range(1, len(a)):
        tmp = a[i]
        while i > 0 and tmp < a[i - 1]:
            a[i] = a[i - 1]
            i -= 1
        a[i] = tmp
