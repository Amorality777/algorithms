def bubble_sort(a: list) -> None:
    """Сортировка пузырьком.

    Args:
        a (list): список для сортировки.
    """
    swapped = True
    n = len(a)
    while swapped:
        swapped = False
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        n -= 1
