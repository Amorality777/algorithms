def find_digits(seq: str) -> int:
    match = {'on': 'one', 'tw': 'two', 'th': 'three', 'fo': 'four', 'fi': 'five', 'si': 'six', 'se': 'seven',
             'ei': 'eight', 'ni': 'nine'}
    digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
              'nine': '9'}

    if not seq:
        return 0
    first = None
    last = None
    for i in range(len(seq) - 1):
        if seq[i].isdigit():
            first = first or seq[i]
            last = seq[i]
        else:
            key = seq[i: i + 2]
            if (expected := match.get(key)) and seq[i:].startswith(expected):
                digit = digits[expected]
                first = first or digit
                last = digit
    # Требуется проверка последнего элемента
    last_char = seq[-1]
    if last_char.isdigit():
        first = first or last_char
        last = last_char
    return int(first + last)
