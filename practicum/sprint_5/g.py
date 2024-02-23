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


def max_path(node):
    if node is None:
        return None, None
    left, m_l = max_path(node.left)
    right, m_r = max_path(node.right)
    best = left
    if right:
        best = left if best and best > right else right
    best = node.value + best if best is not None and best > 0 else node.value
    best = max(best, node.value)
    curr = node.value
    if left and left >= 0:
        curr += left
    if right and right >= 0:
        curr += right
    mx = curr
    if m_l is not None:
        mx = max(mx, m_l)
    if m_r is not None:
        mx = max(mx, m_r)
    return best, mx


def solution(root) -> int:
    return int(max(max_path(root)))


def test():
    node14 = Node(-1, None, None)
    node13 = Node(-8, None, None)
    node12 = Node(-6777, None, None)
    node11 = Node(-7, None, None)
    node10 = Node(-12, None, None)
    node9 = Node(-10, None, None)
    node8 = Node(-2666, None, None)
    node7 = Node(-3, None, None)
    node6 = Node(-1005, node13, node14)
    node5 = Node(0, node11, node12)
    node4 = Node(-4555, node9, node10)
    node3 = Node(-3, node7, node8)
    node2 = Node(-1, node5, node6)
    node1 = Node(-112, node3, node4)
    node0 = Node(-105, node1, node2)
    print(solution(node0))
    assert 0 == solution(node0)


if __name__ == '__main__':
    test()
