import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def traverse_tree(root):
    if root is None:
        return ['']
    res = []
    if root.left is not None:
        res += traverse_tree(root.left)
    if root.right is not None:
        res += traverse_tree(root.right)

    if not res:
        return [f'{root.value}']
    return [f'{root.value}{r}' for r in res]


def solution(root) -> int:
    res = traverse_tree(root)
    return sum(map(int, res))


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275


if __name__ == '__main__':
    test()
