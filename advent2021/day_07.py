from functools import lru_cache
from typing import List, Callable


def part1(data: List[int], x: int) -> int:
    return sum([(abs(x - i)) for i in data])


@lru_cache(maxsize=4096)
def spent(steps):
    return sum([i for i in range(abs(steps) + 1)])


def part2(data: List[int], x: int) -> int:
    return sum([(spent(x - i)) for i in data])


def fuel_spent(data: List[int], func: Callable) -> int:
    mini = min(data)
    maxi = max(data)

    position = min(range(mini, maxi + 1), key=lambda x: func(data, x))
    return func(data, position)


if __name__ == "__main__":
    data = []
    with open("../inputs/day_07.txt") as infile:
        for line in infile:
            data.append(int(line.strip()))

    print(fuel_spent(data, part1))
    print(fuel_spent(data, part2))
