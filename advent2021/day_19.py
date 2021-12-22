import math
from typing import List, Tuple


POINT = Tuple[int, int, int]


def parse(data: List[str]) -> List[List[POINT]]:
    results = []
    pos = 0

    for i, row in enumerate(data):
        if row.strip() == "":
            results.append([tuple([int(x) for x in y.strip().split(",")]) for y in data[pos:i]])
        if row.startswith("---"):
            pos = i + 1

    return results  # type: ignore


def distance(x: POINT, y: POINT) -> float:
    return math.sqrt(sum([math.pow(i - j, 2) for i, j in zip(x, y)]))


def distances(scanner: List[POINT]) -> List[List[float]]:
    return [[distance(scanner[i], scanner[j]) for j in range(len(scanner))] for i in range(len(scanner))]


def overlapping(dist1: List[List[float]], dist2: List[List[float]]) -> List[Tuple[int, int]]:
    for row2 in dist2:
        for row1 in dist1:
            matching = []

            for i, x in enumerate(row1):
                if x in row2:
                    matching.append((i, row2.index(x)))

            if len(matching) >= 12:
                return matching

    return []


def rotation(points1: List[POINT], points2: List[POINT]):
    def almost_zero(data):
        return {round(x, 6) for x in data}

    transformations = [
        ([2, 0, 1], [-1, -1, 1]), ([0, 1, 2], [1, -1, -1]), ([2, 1, 0], [-1, -1, -1]), ([2, 1, 0], [1, -1, 1]),
        ([0, 2, 1], [-1, -1, -1]), ([1, 2, 0], [1, -1, -1]), ([1, 0, 2], [-1, -1, -1]), ([1, 2, 0], [1, 1, 1]),
        ([0, 2, 1], [-1, 1, 1]), ([0, 1, 2], [-1, 1, -1]), ([0, 2, 1], [1, -1, 1]), ([2, 0, 1], [-1, 1, -1]),
        ([1, 0, 2], [1, 1, -1]), ([2, 1, 0], [1, 1, -1]), ([2, 0, 1], [1, 1, 1]), ([2, 1, 0], [-1, 1, 1]),
        ([0, 1, 2], [1, 1, 1]), ([1, 0, 2], [1, -1, 1]), ([1, 0, 2], [-1, 1, 1]), ([0, 1, 2], [-1, -1, 1]),
        ([1, 2, 0], [-1, 1, -1]), ([1, 2, 0], [-1, -1, 1]), ([0, 2, 1], [1, 1, -1]), ([2, 0, 1], [1, -1, -1])
    ]

    for indexes, signs in transformations:
        p1, p2, p3 = indexes
        s1, s2, s3 = signs

        error_x = almost_zero([x[0] - y[p1] * s1 for x, y in zip(points1, points2)])
        error_y = almost_zero([x[1] - y[p2] * s2 for x, y in zip(points1, points2)])
        error_z = almost_zero([round(x[2] - y[p3] * s3, 8) for x, y in zip(points1, points2)])

        if len(error_x) == 1 and len(error_y) == 1 and len(error_z) == 1:
            errors = (error_x.pop(), error_y.pop(), error_z.pop())
            return indexes, signs, errors

    raise ValueError("No matching was found")


def transform(points: List[POINT], transform: List[int], sign: List[int], translate: List[int]) -> List[POINT]:
    def fix(x): return round(x)
    return [
        (fix(p[transform[0]] * sign[0] + translate[0]),
         fix(p[transform[1]] * sign[1] + translate[1]),
         fix(p[transform[2]] * sign[2] + translate[2])) for p in points
    ]


def beacons(scanners: List[List[POINT]]) -> Tuple[int, int]:
    points = scanners[0]
    dist = distances(points)
    to_check = list(range(1, len(scanners)))
    pos = []

    for j in to_check:
        add_dist = distances(scanners[j])
        matching = overlapping(dist, add_dist)

        if len(matching) < 12:
            to_check.append(j)
            continue

        match1 = [points[x] for x, _ in matching]
        match2 = [scanners[j][x] for _, x in matching]

        rot, s, tran = rotation(match1, match2)
        norm_points = transform(scanners[j], rot, s, tran)

        points += [p for p in norm_points if p not in points]
        dist = distances(points)
        pos.append(tran)

    scanner_distances = []
    for i in range(len(pos)):
        for j in range(len(pos)):
            scanner_distances.append(sum([abs(x - y) for x, y in zip(pos[i], pos[j])]))

    return len(dist), max(scanner_distances)


if __name__ == "__main__":
    with open("../inputs/day_19.txt") as infile:
        data = parse(infile.readlines())

    print(beacons(data))
