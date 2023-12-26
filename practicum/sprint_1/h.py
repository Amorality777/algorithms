n = int(input())


# 36

def is_four_pow(num: int) -> bool:
    while num > 4:
        num, mod = divmod(num, 4)
        if mod != 0:
            return False
    return num == 4


print(is_four_pow(n))