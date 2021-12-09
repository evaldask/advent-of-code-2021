from collections import Counter
from typing import List, Tuple
from typing import Counter as typedCounter


TUPLE_INT = Tuple[int, int]
PAIR = Tuple[TUPLE_INT, TUPLE_INT]


def parse(data: List[str]) -> List[PAIR]:
    def fmt(coords):
        parts = coords.split(",")
        assert 2 == len(parts)
        return (int(parts[0]), int(parts[1]))

    results = []

    for row in data:
        splitted = row.strip().split("->")
        assert 2 == len(splitted)

        results.append((fmt(splitted[0]), fmt(splitted[1])))

    return results


def vents_map(data: List[PAIR]) -> int:
    mapped: typedCounter[TUPLE_INT] = Counter()

    for ((x1, y1), (x2, y2)) in data:
        if x1 != x2 and y1 != y2:
            continue

        for i in range(min(x1, x2), max(x1, x2) + 1):
            for j in range(min(y1, y2), max(y1, y2) + 1):
                mapped[(i, j)] += 1

    return sum([True for _, j in mapped.most_common() if j > 1])


def diagonal(data: List[PAIR]):
    mapped: typedCounter[TUPLE_INT] = Counter()

    for ((x1, y1), (x2, y2)) in data:
        dir1 = 1 if max(x1, x2) == x2 else -1
        dir2 = 1 if max(y1, y2) == y2 else -1

        r1 = range(x1, x2 + dir1, dir1)
        r2 = range(y1, y2 + dir2, dir2)

        if x1 != x2 and y1 != y2:
            for i, j in zip(r1, r2):
                mapped[(i, j)] += 1

        else:
            for i in r1:
                for j in r2:
                    mapped[(i, j)] += 1

    return sum([True for _, j in mapped.most_common() if j > 1])


if __name__ == "__main__":
    with open("../inputs/day_05.txt") as infile:
        data = infile.readlines()

    coords = parse(data)
    print(vents_map(coords))
    print(diagonal(coords))
