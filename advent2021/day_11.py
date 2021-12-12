import itertools
from typing import List, Generator


def parse(data: List[str]) -> List[List[int]]:
    return [[int(y) for y in x.strip()] for x in data]


def flash_step(data: List[List[int]], steps) -> Generator[int, None, None]:
    for _ in range(steps):
        data = [[y + 1 for y in x] for x in data]
        mask = [[False for _ in range(10)] for _ in range(10)]

        changes = True
        while changes:
            changes = False
            for x, y in itertools.product(range(10), repeat=2):
                if data[x][y] > 9 and mask[x][y] is False:
                    mask[x][y] = True
                    for xx, yy in itertools.product(range(-1, 2), repeat=2):
                        if 0 <= x + xx < 10 and 0 <= y + yy < 10:
                            data[x + xx][y + yy] += 1

                    changes = True

        flashes = 0
        for x, y in itertools.product(range(10), repeat=2):
            if data[x][y] > 9:
                data[x][y] = 0
                flashes += 1

        yield flashes


def count_flashes(data: List[List[int]], steps: int) -> int:
    total = 0

    for flashed in flash_step(data, steps):
        total += flashed

    return total


def sync_flashes(data: List[List[int]], steps: int) -> int:
    for i, flashed in enumerate(flash_step(data, steps)):
        if flashed == 100:
            return i + 1
    return -1


if __name__ == "__main__":
    with open("../inputs/day_11.txt") as infile:
        data = parse(infile.readlines())

    print(count_flashes(data, 100))
    print(sync_flashes(data, 1000))
