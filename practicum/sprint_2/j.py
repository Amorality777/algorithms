class Node:
    def __init__(self, value, node=None):
        self.next_node: Node = node
        self.value = value

    @staticmethod
    def put(head, value):
        last_node = Node(value)
        if head is None:
            head = last_node
        else:
            node = head
            while node.next_node:
                node = node.next_node
            node.next_node = last_node
        return head

    @staticmethod
    def get(head):
        if head is None:
            print('error')
            return
        print(head.value)
        return head.next_node

    @staticmethod
    def size(node) -> None:
        s = 0
        while node:
            node = node.next_node
            s += 1
        print(s)


def main():
    n = int(input())

    head = None
    for _ in range(n):
        command = input()
        if command.startswith('p'):
            command, value = command.split()
            head = Node.put(head, value)
        elif command.startswith('g'):
            head = getattr(Node, command)(head)
        else:
            getattr(Node, command)(head)


main()
