import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0, size=0):
            self.right = right
            self.left = left
            self.value = value
            self.size = size


def calculate_sizes(root):
    if root is None:
        return 0
    root.size = 1 + calculate_sizes(root.left) + calculate_sizes(root.right)
    return root.size


def find_kth(root, k):
    left_size = 0 if root.left is None else root.left.size
    if left_size == k:
        return root.value
    if left_size < k:
        return find_kth(root.right, k - left_size - 1)
    return find_kth(root.left, k)


def get_size(node):
    return node.size if node else 0


def split(root, k) -> tuple:
    if root is None:
        # Подумайте, что надо вернуть в таком случае.
        return None, None
    if get_size(root.left) + 1 <= k:
        k -= 1 + get_size(root.left)
        root.right, right_side = split(root.right, k)
        return root, right_side
    # Что должно происходить при спуске рекурсии в левое поддерево?
    return split(root.left, k)


def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert (left.size == 4)
    assert (right.size == 2)


if __name__ == '__main__':
    test()
