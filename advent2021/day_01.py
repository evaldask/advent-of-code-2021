from typing import List


def parse(data: List[str]) -> List[int]:
    return [int(x.strip()) for x in data]


def larger(data: List[int]) -> int:
    counter = 0

    for v1, v2 in zip(data, data[1:]):
        if v2 > v1:
            counter += 1

    return counter


def larger3(data: List[int]) -> int:
    counter = 0
    prev = 1e9

    for i in range(len(data) - 2):
        total = sum(data[i: i + 3])
        if total > prev:
            counter += 1

        prev = total

    return counter


if __name__ == "__main__":
    with open("../inputs/day_01.txt") as infile:
        data = infile.readlines()

    parsed = parse(data)
    print(larger(parsed))
    print(larger3(parsed))
