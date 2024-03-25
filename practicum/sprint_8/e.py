import sys


def main():
    s = sys.stdin.readline().strip()
    results = []
    for _ in range(int(input())):
        p, i = sys.stdin.readline().rstrip().split()
        results.append((int(i), p))
    results.sort()
    ans = []
    prev = 0
    if results:
        for pos, sub in results:
            ans.extend(([s[prev:pos], sub]))
            prev = pos
        ans.append(s[pos:])
    print(''.join(ans))


main()
