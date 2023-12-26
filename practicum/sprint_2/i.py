class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, value) -> None:
        if self._size == self.max_n:
            print('error')
            return
        self.queue[self.tail] = value
        self.tail = (1 + self.tail) % self.max_n
        self._size += 1

    def peek(self) -> None:
        if self.is_empty():
            print('None')
            return
        print(self.queue[self.head])

    def pop(self) -> None:
        if self.is_empty():
            print('None')
            return
        print(self.queue[self.head])
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self._size -= 1

    def size(self):
        print(self._size)


def main():
    commands = int(input())
    size = int(input())

    queue = Queue(size)

    for _ in range(commands):
        command = input()
        if command.startswith('pu'):
            command, value = command.split()
            getattr(queue, command)(value)
        else:
            getattr(queue, command)()


if __name__ == '__main__':
    main()
