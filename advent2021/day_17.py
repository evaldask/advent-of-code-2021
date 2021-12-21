from typing import Tuple


COORDS = Tuple[int, int]


def parse(line: str) -> Tuple[COORDS, COORDS]:
    parsed = [tuple([int(y) for y in x.split("=")[1].split("..")]) for x in line.split(", ")]
    return parsed[0], parsed[1]  # type: ignore


def trajectory(x: COORDS, y: COORDS) -> COORDS:
    best = 0
    possible_shots = 0

    for xx in range(1, x[1] + 1):
        for yy in range(y[0], abs(y[0])):
            speed_x, speed_y = xx, yy
            coord_x, coord_y, velocity = 0, 0, 0

            while coord_y >= y[0] and coord_x < x[1]:
                coord_x += speed_x
                coord_y += speed_y
                velocity += speed_y if speed_y > 0 else 0
                speed_x = max(0, speed_x - 1)
                speed_y -= 1

                if y[0] <= coord_y <= y[1] and x[0] <= coord_x <= x[1]:
                    best = max(best, velocity)
                    possible_shots += 1
                    break

    return best, possible_shots


if __name__ == "__main__":
    with open("../inputs/day_17.txt") as infile:
        x, y = parse(infile.read().strip())
    print(trajectory(x, y))
