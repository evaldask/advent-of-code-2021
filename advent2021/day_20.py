import itertools
from typing import List, Tuple, Set


def parse(data: List[str]) -> Tuple[Set[int], Set[Tuple[int, int]]]:
    commands = {i for i, x in enumerate(data[0].strip()) if x == "#"}

    pos = set()
    for i, row in enumerate(data[2:]):
        for j, value in enumerate(row):
            if value == "#":
                pos.add((i, j))

    return commands, pos


def process(image: Set[Tuple[int, int]], commands: Set[int], iterations: int) -> int:
    coords = [-1, 0, 1]
    for cycle in range(iterations):
        new_img = set()

        x1, x2 = min(image, key=lambda x: x[0])[0], max(image, key=lambda x: x[0])[0]
        y1, y2 = min(image, key=lambda x: x[1])[1], max(image, key=lambda x: x[1])[1]

        for i in range(x1 - 1, x2 + 2):
            for j in range(y1 - 1, y2 + 2):
                index = 0

                for x, y in itertools.product(coords, repeat=2):
                    if x1 <= i + x <= x2 and y1 <= j + y <= y2:
                        index = index << 1 | ((i + x, j + y) in image)
                    else:
                        index = index << 1 | (cycle % 2 == 1)

                if index in commands:
                    new_img.add((i, j))

        image = new_img

    return len(image)


if __name__ == "__main__":
    with open("../inputs/day_20.txt") as infile:
        commands, image = parse(infile.readlines())

    print(process(image, commands, 2))
    print(process(image, commands, 50))
