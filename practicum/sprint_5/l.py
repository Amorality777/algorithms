def sift_down(heap, idx) -> int:
    l = idx * 2
    r = idx * 2 + 1

    if len(heap) <= l:
        return idx
    if r < len(heap) and heap[l] < heap[r]:
        index_largest = r
    else:
        index_largest = l

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)

    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5
    sample = [90, 70, 50]
    assert sift_down(sample, 1) == 1


if __name__ == '__main__':
    test()
