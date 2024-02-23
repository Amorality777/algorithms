import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def traverse(root, arr: list):
    if root is None:
        return
    traverse(root.left, arr)
    arr.append(root.value)
    traverse(root.right, arr)


def solution(root1, root2) -> bool:
    f = []
    traverse(root1, f)
    s = []
    traverse(root2, s)
    return f == s


def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()
