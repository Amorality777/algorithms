import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left

        def __repr__(self):
            return str(self.value)


def height(root) -> int:
    if not root:
        return 0
    left = height(root.left)
    if left == -1:
        return -1
    right = height(root.right)
    if right == -1:
        return -1
    if abs(left - right) > 1:
        return -1

    return max(left, right) + 1


def solution(root) -> bool:
    h = height(root)
    return h != -1


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
