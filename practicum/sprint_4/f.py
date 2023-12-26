from collections import defaultdict


def main():
    input()
    words = input().split()
    result = defaultdict(list)

    for i, word in enumerate(words):
        key = ''.join(sorted(word))
        result[key].append(i)
    for values in result.values():
        print(*sorted(values))


main()
