from collections import Counter
from typing import List, Tuple
from typing import Counter as typedCounter


def parse(data: List[str]) -> List[List[int]]:
    matrix = []

    for row in data:
        line = []
        for item in row.strip():
            line.append(int(item))
        matrix.append(line)

    return matrix


def get_lowest_points(data: List[List[int]]) -> List[Tuple[int, int]]:
    potential = []

    for i, row in enumerate(data):
        positions = sorted(range(len(row)), key=lambda x: row[x])
        reserved = []
        for pos in positions:
            if pos + 1 in reserved or pos - 1 in reserved:
                continue

            cond1 = row[pos - 1] > row[pos] if pos - 1 >= 0 else True
            cond2 = row[pos + 1] > row[pos] if pos + 1 < len(row) else True
            if cond1 and cond2:
                reserved.append(pos)
                potential.append((i, pos))

    coords = []
    for x, y in potential:
        value = data[x][y]
        cond1 = data[x-1][y] > value if x - 1 >= 0 else True
        cond2 = data[x+1][y] > value if x + 1 < len(data) else True
        if cond1 and cond2:
            coords.append((x, y))

    return coords


def low_points(data: List[List[int]]) -> int:
    total = 0
    for x, y in get_lowest_points(data):
        total += data[x][y] + 1
    return total


def basins(data: List[List[int]]) -> int:
    row_size = len(data[0])
    col_size = len(data)

    def fill(x, y, value):
        if x < 0 or x >= col_size:
            return

        if y < 0 or y >= row_size:
            return

        if data[x][y] == value or data[x][y] == 9 or data[x][y] < 0:
            return

        data[x][y] = value
        fill(x-1, y, value)
        fill(x+1, y, value)
        fill(x, y-1, value)
        fill(x, y+1, value)

    coords = get_lowest_points(data)
    for i, (x, y) in enumerate(coords):
        fill(x, y, (i + 1) * -1)

    c: typedCounter[int] = Counter()
    for row in data:
        c.update(row)

    del c[9]
    total = 1
    for _, s in c.most_common(3):
        total *= s

    return total


if __name__ == "__main__":
    with open("../inputs/day_09.txt") as infile:
        data = infile.readlines()

    parsed = parse(data)
    print(low_points(parsed))
    print(basins(parsed))
