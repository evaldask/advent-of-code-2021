from typing import Tuple, List


COORD = Tuple[int, int, int]
ROW = Tuple[int, Tuple[int, int], Tuple[int, int], Tuple[int, int]]


def parse(row: str) -> ROW:
    command, coords = row.strip().split(" ")
    result = [1 if command == "on" else -1]

    for pair in coords.split(","):
        left, right = pair.split("=")[1].split("..")
        result.append((int(left), int(right)))  # type: ignore

    return tuple(result)  # type: ignore


def boundaries(c1, c2):
    return -50 <= c1 <= c2 <= 50


def cuboids(cubs: List[ROW], action: ROW, part1: bool = False) -> List[ROW]:
    op, (a1, a2), (b1, b2), (c1, c2) = action

    if part1 is True:
        inside = boundaries(a1, a2) and boundaries(b1, b2) and boundaries(c1, c2)
        if not inside:
            return cubs

    for i in range(len(cubs)):
        sign, (x1, x2), (y1, y2), (z1, z2) = cubs[i]

        dx1, dx2 = max(x1, a1), min(x2, a2)
        dy1, dy2 = max(y1, b1), min(y2, b2)
        dz1, dz2 = max(z1, c1), min(z2, c2)

        if dx1 <= dx2 and dy1 <= dy2 and dz1 <= dz2:
            cubs.append((sign * -1, (dx1, dx2), (dy1, dy2), (dz1, dz2)))

    if op > 0:
        cubs.append(action)

    return cubs


def sumup(cubs: List[ROW]) -> int:
    total = 0
    for sign, (x1, x2), (y1, y2), (z1, z2) in cubs:
        total += sign * (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)

    return total


if __name__ == "__main__":
    coords1: List[ROW] = []
    coords2: List[ROW] = []
    with open("../inputs/day_22.txt") as infile:
        for line in infile:
            row = parse(line)
            coords1 = cuboids(coords1, row, part1=True)
            coords2 = cuboids(coords2, row)

    print(sumup(coords1))
    print(sumup(coords2))
