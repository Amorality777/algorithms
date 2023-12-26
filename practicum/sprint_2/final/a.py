"""
https://contest.yandex.ru/contest/22781/run-report/99915189/
-- ПРИНЦИП РАБОТЫ --
Алгоритм реализован на двустороннем кольцевом буфере, что позволяет при инициализации выделить
необходимый объем памяти под очередь и сократить издержки расширения массива во время работы.
Для поддержания быстродействия команд при каждом действии обновляются счетчики общего состояния очереди.
Алгоритм имеет ограничение на кол-во добавления элементов в очередь.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность одной команды О(1), общее время работы зависит от кол-ва команд и = О(n)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(m), где m - ограничение максимальной длины очереди.
"""


class RingDeque:

    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = max_size

    def push_front(self, value: str):
        self._check_space()

        self.head = self._shift_left(self.head)
        self.queue[self.head] = value
        self.size += 1

    def push_back(self, value: str):
        self._check_space()

        self.queue[self.tail] = value
        self.tail = self._shift_right(self.tail)
        self.size += 1

    def pop_front(self) -> str:
        self._check_not_empty()

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = self._shift_right(self.head)
        self.size -= 1
        return value

    def pop_back(self):
        self._check_not_empty()

        self.tail = self._shift_left(self.tail)
        value = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        return value

    def _shift_left(self, index: int) -> int:
        """Сдвиг индекса влево."""
        return self.max_size - 1 if index == 0 else index - 1

    def _shift_right(self, index: int) -> int:
        """Сдвиг индекса вправо."""
        return (index + 1) % self.max_size

    def _check_space(self) -> None:
        """Проверка наличия места в очереди."""
        if self.size == self.max_size:
            raise IndexError('Not enough space')

    def _check_not_empty(self) -> None:
        """Проверка наличия элементов в очереди."""
        if self.size == 0:
            raise IndexError('Queue is empty')


def main():
    commands_count = int(input())
    size = int(input())
    deque = RingDeque(size)
    for _ in range(commands_count):
        command = input()
        try:
            if command.startswith('pop'):
                value = getattr(deque, command)()
                print(value)
            else:
                command, value = command.split()
                getattr(deque, command)(value)
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()
