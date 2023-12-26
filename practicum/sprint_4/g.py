import sys


def main():
    input()
    seq = sys.stdin.readline().rstrip().split()
    match = {'0': -1, '1': 1}
    infos = []
    results = set()
    for value in seq:
        value = match[value]
        for j, info in enumerate(infos):
            info = (info[0] + value, info[1] + 1)
            if info[0] == 0:
                results.add(info[1])
            infos[j] = info
        infos.append((value, 1))

    return max(results) if results else 0


print(main())
