import heapq
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

    def cost(self, x: int, y: int) -> int:
        add = x // self.bound_x + y // self.bound_y
        coord_x = x % self.bound_x
        coord_y = y % self.bound_y
        value = (self.data[coord_x][coord_y] + add - 1) % 9 + 1

        return value


def navigate(map: Map) -> int:
    seen = {(0, 0)}
    to_visit = [(0, 0, 0)]

    while to_visit:
        cost, x, y = heapq.heappop(to_visit)

        if (x, y) == map.finish():
            return cost

        for nx, ny in map.neighbours(x, y):
            current_cost = cost + map.cost(nx, ny)
            if (nx, ny) not in seen:
                heapq.heappush(to_visit, (current_cost, nx, ny))
                seen.add((nx, ny))

    return -1


if __name__ == "__main__":
    with open("../inputs/day_15.txt") as infile:
        data = parse(infile.readlines())

    print(navigate(Map(data, 1)))
    print(navigate(Map(data, 5)))
