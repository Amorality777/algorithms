GOOD_DISTANCE = 20 * 20


class Point:
    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)

    def get_dist_pow(self, point) -> int:
        return (self.x - point.x) ** 2 + (self.y - point.y) ** 2


def main():
    stations = []
    for _ in range(int(input())):
        stations.append(Point(*input().split()))

    bus_stops = []
    for _ in range(int(input())):
        bus_stops.append(Point(*input().split()))

    best = 0
    ans = 0
    for i, point in enumerate(stations, 1):
        score = 0
        for bus_stop in bus_stops:
            if point.get_dist_pow(bus_stop) <= GOOD_DISTANCE:
                score += 1
        if score > best:
            best = score
            ans = i
    print(ans)


main()
