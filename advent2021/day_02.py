from typing import List, Tuple


def parse(data: List[str]) -> List[Tuple[str, int]]:
    res = []

    for row in data:
        splitted = row.strip().split(" ")
        res.append((splitted[0], int(splitted[1])))

    return res


def position(inputs: List[Tuple[str, int]]) -> int:
    forward = 0
    depth = 0

    for direction, step in inputs:
        if direction == "forward":
            forward += step
        elif direction == "down":
            depth += step
        elif direction == "up":
            depth -= step

    return depth * forward


def aim(inputs: List[Tuple[str, int]]) -> int:
    forward = 0
    depth = 0
    aim_pos = 0

    for direction, step in inputs:
        if direction == "forward":
            forward += step
            depth += aim_pos * step
        elif direction == "down":
            aim_pos += step
        elif direction == "up":
            aim_pos -= step

    return depth * forward


if __name__ == "__main__":
    with open("../inputs/day_02.txt") as infile:
        data = infile.readlines()

    parsed = parse(data)
    print(position(parsed))
    print(aim(parsed))
