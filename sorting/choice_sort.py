def choice_sort(a: list) -> None:
    """Сортировка выбором.

    Args:
        a (list): список для сортировки.
    """
    for pos in range(len(a)):
        for k in range(pos + 1, len(a)):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
