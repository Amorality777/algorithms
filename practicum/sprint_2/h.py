class Stack:
    def __init__(self):
        self.steck = []

    def push(self, value: str) -> None:
        self.steck.append(value)

    def pop(self) -> str:
        return self.steck.pop()

    def is_empty(self) -> bool:
        return not bool(self.steck)


def is_correct_bracket_seq(seq: str) -> bool:
    match = {'(': ')', '{': '}', '[': ']'}
    stack = Stack()
    for bracket in seq:
        if close := match.get(bracket):
            stack.push(close)
        else:
            if stack.is_empty() or stack.pop() != bracket:
                return False

    return stack.is_empty()


print(is_correct_bracket_seq(input()))
