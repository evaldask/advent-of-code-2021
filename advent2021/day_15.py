from typing import List, Tuple, Generator


COORDS = Tuple[int, int]


def parse(data: List[str]) -> List[List[int]]:
    return [[int(x) for x in r.strip()] for r in data]


class Map:
    def __init__(self, data: List[List[int]], scale: int = 1):
        self.data = data
        self.scale = scale

        self.bound_x = len(self.data)
        self.bound_y = len(self.data[0])
        self.lim_x = len(self.data) * self.scale
        self.lim_y = len(self.data[0]) * self.scale

    def neighbours(self, x: int, y: int) -> Generator[COORDS, None, None]:
        for xx, yy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= x + xx < self.lim_x and 0 <= y + yy < self.lim_y:
                yield x + xx, y + yy

    def finish(self) -> COORDS:
        return self.lim_y - 1, self.lim_y - 1

    def start(self) -> COORDS:
        return 0, 0

    def cost(self, x: int, y: int) -> int:
        add = x // self.bound_x + y // self.bound_y
        coord_x = x % self.bound_x
        coord_y = y % self.bound_y
        value = (self.data[coord_x][coord_y] + add - 1) % 9 + 1

        return value


def navigate(map: Map) -> int:
    paths = {}
    costs = {map.start(): 0}
    to_visit = [map.start()]

    while to_visit:
        pos = min(to_visit, key=lambda x: costs.get(x, 1_000_000_000))
        to_visit.remove(pos)

        if pos == map.finish():
            break

        for npos in map.neighbours(*pos):
            current_cost = costs[pos] + map.cost(*npos)
            if current_cost >= costs.get(npos, 1_000_000_000):
                continue

            paths[npos] = pos
            costs[npos] = current_cost

            if npos not in to_visit:
                to_visit.append(npos)

    return costs[map.finish()]


if __name__ == "__main__":
    with open("../inputs/day_15.txt") as infile:
        data = parse(infile.readlines())

    print(navigate(Map(data, 1)))
    print(navigate(Map(data, 5)))
