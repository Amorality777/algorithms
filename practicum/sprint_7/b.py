def to_seconds(exp: str) -> int:
    if '.' in exp:
        h, m = exp.split('.')
        return int(h) * 60 + int(m)
    return int(exp) * 60


def to_hours(seconds: int) -> str:
    h, m = divmod(seconds, 60)
    if m:
        return f'{h}.{m}'
    return str(h)


def get_input() -> list[tuple[int, int]]:
    schedule = []
    for _ in range(int(input())):
        start, end = input().split()
        schedule.append((to_seconds(end), to_seconds(start)))

    return schedule


def main():
    schedule = get_input()
    schedule.sort(reverse=True)

    result = []
    end = 0
    while schedule:
        quick = schedule.pop()
        if quick[1] >= end:
            result.append(quick)
            end = quick[0]

    print(len(result))
    for end, start in result:
        print(f'{to_hours(start)} {to_hours(end)}')


main()
