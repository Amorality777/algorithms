def sift_up(heap, idx) -> int:
    parent = idx // 2
    if parent >= 1 and heap[idx] > heap[parent]:
        heap[idx], heap[parent] = heap[parent], heap[idx]
        return sift_up(heap, parent)
    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()
