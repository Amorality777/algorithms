def main():
    first = input()
    second = input()
    if len(first) != len(second):
        return 'NO'
    match = {}
    values = []

    for f, s in zip(first, second):
        if f in match:
            m = match[f]
            if m != s:
                return 'NO'
        else:
            if s in values:
                return 'NO'
            match[f] = s
            values.append(s)
    return 'YES'


if __name__ == '__main__':
    print(main())
