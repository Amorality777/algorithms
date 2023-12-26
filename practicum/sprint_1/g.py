num = int(input())


def hex_to_binary(n: int) -> str:
    if not n:
        return str(n)
    result = ''
    while n > 0:
        n, m = divmod(n, 2)
        result = f'{m}{result}'

    return result


print(hex_to_binary(num))
