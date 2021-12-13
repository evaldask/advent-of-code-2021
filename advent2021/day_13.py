from typing import List, Tuple, Set


COORDS = Set[Tuple[int, int]]
FOLDS = List[Tuple[str, int]]


def parse(data: List[str]) -> Tuple[COORDS, FOLDS]:
    coords = []
    folds = []

    for row in data:
        if len(row.strip()) == 0:
            continue

        if row.startswith("fold along"):
            splitted = row.strip().replace("fold along ", "").split("=")
            assert 2 == len(splitted)
            folds.append((splitted[0], int(splitted[1])))
        else:
            splitted = row.strip().split(",")
            assert 2 == len(splitted)
            coords.append((int(splitted[0]), int(splitted[1])))

    return set(coords), folds


def fold(coords: COORDS, folds: FOLDS, show=False) -> int:
    for axis, split_point in folds:
        new_coords = []

        range_x = max(coords, key=lambda x: x[0])[0]
        range_y = max(coords, key=lambda x: x[1])[1]

        for x, y in coords:
            if axis == "x" and x > split_point:
                new_coords.append((range_x - x, y))
            elif axis == "y" and y > split_point:
                new_coords.append((x, range_y - y))
            else:
                new_coords.append((x, y))

        coords = set(new_coords)

    if show:
        range_x = max(coords, key=lambda x: x[0])[0] + 1
        range_y = max(coords, key=lambda x: x[1])[1] + 1
        for y in range(range_y):
            row = ["#" if (x, y) in coords else " " for x in range(range_x)]
            print("".join(row))

    return len(coords)


if __name__ == "__main__":
    with open("../inputs/day_13.txt") as infile:
        coords, folds = parse(infile.readlines())

    print(fold(coords, folds[:1]))
    fold(coords, folds, show=True)
