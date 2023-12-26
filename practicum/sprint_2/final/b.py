"""
https://contest.yandex.ru/contest/22781/run-report/99681290/
-- ПРИНЦИП РАБОТЫ --
Алгоритм реализован на стеке и встроенном модуле operator.
Выполняется поэтапный обход элементов входной последовательности, если получается привести элемент к целому числу,
то он добавляется на вершину стека,
иначе считается операцией, и тогда полученная операция выполняется над двумя последними элементами в стеке,
полученный результат кладется на вершину стека.

Логика повторяется для каждого элемента.

После обработки последовательности выводится число, лежащее на вершине стека.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сложность вставки в конец стека и удаления с вершины (конца массива) О(1).
Один элемент последовательности будет вставлен и удален из стека не более одного раза,
общая сложность алгоритма О(n), где n - кол-во команд.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
О(n), где n - кол-во элементов в массиве (худший случай, где все элементы - числа).
"""
from operator import add, floordiv, mul, sub


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int:
        return self.stack.pop()


def main():
    operators = {'+': add, '-': sub, '*': mul, '/': floordiv}
    expression = input().split()

    stack = Stack()
    for operand in expression:
        try:
            digit = int(operand)
            stack.push(digit)
        except ValueError:
            right = stack.pop()
            left = stack.pop()
            stack.push(operators.get(operand)(left, right))
    print(stack.pop())


if __name__ == '__main__':
    main()
