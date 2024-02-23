"""
https://contest.yandex.ru/contest/24810/run-report/105465228/
-- ПРИНЦИП РАБОТЫ --
1. Поиск ноды удаления + фиксация родителя удаляемой ноды
2. Замена в зависимости от наличия у удаляемой ноды детей.
 1. Детей нет => если это был корень, то дерево удалено root=None, иначе удаление детей родителя
 2. Оба ребенка есть => находим у правого ребенка самый левый элемент, сохраняем значение,
    удаляем элемент рекурсивно (у него не более одного ребенка), присваиваем удаляемому элементу сохраненное значение.
 3. Только один ребенок => если корень, то ребенок становится новым корнем, иначе родителю вместо удаляемого
    элемента присваивается ребенок

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(h), где h - высота дерева
-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(1)
"""
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value

        def __repr__(self):
            return str(self.value)
else:
    from node import Node


def get_left(node):
    while node.left is not None:
        node = node.left
    return node


def remove(root, key):
    parent = None
    curr = root
    while curr is not None and curr.value != key:
        parent = curr
        curr = curr.left if curr.value > key else curr.right

    if curr is None:
        return root

    if curr.left is None and curr.right is None:
        if curr == root:
            root = None
        else:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
    elif curr.left and curr.right:
        replacement = get_left(curr.right)
        val = replacement.value
        remove(root, val)
        curr.value = val
    else:
        child = curr.left if curr.left is not None else curr.right
        if curr == root:
            root = child
        else:
            if parent.left == curr:
                parent.left = child
            else:
                parent.right = child

    return root


def test():
    node2 = Node(None, None, 2)
    node1 = Node(None, node2, 1)
    newHead = remove(node1, 1)
    assert newHead.value == 2
    assert newHead.right is None


if __name__ == '__main__':
    test()
