from typing import List


def parse(data: List[str]) -> List[List[str]]:
    return [list(x.strip()) for x in data]


def move(data: List[List[str]]) -> int:
    moved = True
    lim_x = len(data)
    lim_y = len(data[0])
    steps = 0

    while moved:
        moved = False
        new = [[z for z in r] for r in data]

        for x, row in enumerate(data):
            for y, v in enumerate(row):
                if v != ".":
                    continue

                left = lim_y - 1 if y - 1 < 0 else y - 1
                down = lim_x - 1 if x - 1 < 0 else x - 1

                if data[x][left] == ">":
                    new[x][left] = "."
                    new[x][y] = ">"
                    moved = True
                    if data[down][left] == "v":
                        new[down][left] = "."
                        new[x][left] = "v"

                elif data[down][y] == "v":
                    new[down][y] = "."
                    new[x][y] = "v"
                    moved = True

        data = new
        steps += 1

    return steps


if __name__ == "__main__":
    with open("../inputs/day_25.txt") as infile:
        data = infile.readlines()

    print(move(parse(data)))
