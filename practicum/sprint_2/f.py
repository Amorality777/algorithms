import sys
import time


class StackMax:
    def __init__(self):
        self.steck = []

    def push(self, value: int):
        max_ = max(self.peek()[1], value) if self.steck else value
        self.steck.append((value, max_))

    def pop(self) -> None:
        try:
            self.steck.pop()
        except IndexError:
            print('error')

    def get_max(self) -> None:
        m = f'{self.peek()[1]}' if self.steck else 'None'
        print(m)

    def peek(self) -> None | tuple:
        if self.steck:
            return self.steck[-1]


def main():
    stack = StackMax()

    n = int(input())
    commands = [sys.stdin.readline().rstrip() for _ in range(n)]

    for command in commands:
        if command.startswith('pu'):
            command, value = command.split()
            getattr(stack, command)(int(value))
        else:
            getattr(stack, command)()


if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
