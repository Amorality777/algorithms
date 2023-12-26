from sys import stdin


def feed_children(hunger_lvls: list, cookies: list) -> int:
    hunger_lvls.sort()
    cookies.sort()
    fed = 0
    cookie_inx = 0
    cookie_count = len(cookies)
    kids_inx = 0
    kids_count = len(hunger_lvls)
    while cookie_inx < cookie_count and kids_inx < kids_count:
        if hunger_lvls[kids_inx] > cookies[cookie_inx]:
            cookie_inx += 1
            continue
        fed += 1
        cookie_inx += 1
        kids_inx += 1

    return fed


def main():
    stdin.readline()
    hunger_lvl = list(map(int, stdin.readline().rstrip().split()))
    stdin.readline()
    cookies = list(map(int, stdin.readline().rstrip().split()))
    print(feed_children(hunger_lvl, cookies))


if __name__ == '__main__':
    main()
