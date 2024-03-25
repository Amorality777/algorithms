def transform(string: str) -> str:
    return ''.join((char for char in string if ord(char) % 2 == 0))


def main() -> None:
    f = transform(input())
    s = transform(input())

    if f == s:
        print('0')
    elif f > s:
        print('1')
    else:
        print('-1')


main()
