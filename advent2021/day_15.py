from typing import List, Tuple, Generator


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

    def neighbours(self, x: int, y: int) -> Generator[Tuple[int, int], None, None]:
        for i in [-1, 1]:
            if 0 <= x + i < self.lim_x:
                yield x + i, y
            if 0 <= y + i < self.lim_y:
                yield x, y + i

    def finish(self, x: int, y: int):
        return x == self.lim_y - 1 and y == self.lim_y - 1

    def start(self) -> Tuple[int, int]:
        return (0, 0)

    def destination(self) -> Tuple[int, int]:
        return (self.lim_y - 1, self.lim_y - 1)

    def cost(self, x: int, y: int) -> int:
        add = x // self.bound_x + y // self.bound_y
        coord_x = x % self.bound_x
        coord_y = y % self.bound_y

        value = self.data[coord_x][coord_y] + add
        if value > 9:
            value -= 9

        if value > 9:
            print(coord_x, coord_y, value)

        return value


def navigate(map: Map) -> int:
    paths = {}
    costs = {map.start(): map.cost(*map.start())}
    to_visit = [map.start()]

    while to_visit:
        pos = min(to_visit, key=lambda x: costs.get(x, 1_000_000_000))
        to_visit.remove(pos)

        if map.finish(*pos):
            break

        for npos in map.neighbours(*pos):
            current_cost = costs[pos] + map.cost(*npos)
            if current_cost >= costs.get(npos, 1_000_000_000):
                continue

            paths[npos] = pos
            costs[npos] = current_cost

            if npos not in to_visit:
                to_visit.append(npos)

    return costs[map.destination()] - costs[map.start()]


if __name__ == "__main__":
    with open("../inputs/day_15.txt") as infile:
        data = parse(infile.readlines())

    print(navigate(Map(data, 1)))
    print(navigate(Map(data, 5)))
