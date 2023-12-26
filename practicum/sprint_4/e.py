def main():
    seq = input()
    if not seq:
        print(0)
        return
    ans = 0
    pos = {}
    left = 0
    i = 0
    for i in range(len(seq)):
        curr = seq[i]
        if curr in pos and pos[curr] >= left:
            ans = max(ans, i - left)
            left = pos[curr] + 1
        pos[curr] = i
    ans = max(ans, i - left + 1)
    print(ans)


main()
