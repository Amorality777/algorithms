# Помогите Васе понять, будет ли фраза палиндромом‎. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.
#
# Решение должно работать за O(N), где N — длина строки на входе.
#
# Формат ввода
# В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не превосходит 20000 символов.
#
# Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.
#
# Формат вывода
# Выведите «True», если фраза является палиндромом, и «False», если не является.
s = input()


def is_palindrome(sent: str) -> bool:
    left = 0
    right = len(sent) - 1
    while left < right:
        if not sent[left].isalnum():
            left += 1
            continue
        if not sent[right].isalnum():
            right -= 1
            continue
        if sent[left].lower() != sent[right].lower():
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome(s))
