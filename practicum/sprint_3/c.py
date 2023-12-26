import sys


def is_substring(sub: str, full: str) -> bool:
    start, end = 0, len(full) - len(sub) + 1
    for char in sub:
        if (i := full.find(char, start, end)) == -1:
            return False
        start = i + 1
        end += 1
    return True


def main():
    print(is_substring(sys.stdin.readline().strip(), sys.stdin.readline().strip()))


if __name__ == '__main__':
    main()
