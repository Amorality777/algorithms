from sys import stdin


def buy_houses(cash: int, houses: list[int]) -> int:
    houses.sort()
    can_buy = 0
    for house_cost in houses:
        cash -= house_cost
        if cash < 0:
            break
        can_buy += 1

    return can_buy


def main():
    n, cash = stdin.readline().split()
    cash = int(cash)
    houses = list(map(int, stdin.readline().rstrip().split()))

    print(buy_houses(cash, houses))


if __name__ == '__main__':
    main()
