def main():
    input()
    stats = (int(cost) for cost in input().split())
    res = 0
    buy = False
    prev = next(stats)
    for cost in stats:
        if not buy and cost > prev:
            buy = True
            res -= prev
        elif buy and cost <= prev:
            buy = False
            res += prev
        prev = cost
    if buy:
        res += prev
    print(res)


main()
