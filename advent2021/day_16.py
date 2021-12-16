import math
from typing import Tuple


def parse(data: str) -> str:
    return "".join([f"{int(x, 16):04b}" for x in data])


def read(data: str, pos: int) -> Tuple[str, int]:
    return data[pos:], int(data[:pos], 2)


def bits(data: str, count: int = 0) -> Tuple[str, int, int]:
    if len(data) < 1:
        return "", count, -1

    data, version = read(data, 3)
    data, packet_type = read(data, 3)

    count += version
    values = []

    if packet_type == 4:
        number = ""
        for i in range(0, len(data)):
            data, first_bit = read(data, 1)
            data, value = read(data, 4)
            number = number + f"{value:04b}"
            if first_bit == 0:
                break

        return data, count, int(number, 2)

    else:
        data, length_type = read(data, 1)
        if length_type == 0:
            data, length = read(data, 15)
            subdata = data[:length]

            while len(subdata) > 0:
                subdata, count, value = bits(subdata, count)
                values.append(value)

            data, _ = read(data, length)

        else:
            data, numbers = read(data, 11)

            for _ in range(numbers):
                data, count, value = bits(data, count)
                values.append(value)

    result = 0
    if packet_type == 0:
        result = sum(values)

    elif packet_type == 1:
        result = math.prod(values)

    elif packet_type == 2:
        result = min(values)

    elif packet_type == 3:
        result = max(values)

    elif packet_type == 5:
        result = int(values[0] > values[1])

    elif packet_type == 6:
        result = int(values[0] < values[1])

    elif packet_type == 7:
        result = int(values[0] == values[1])

    return data, count, result


if __name__ == "__main__":
    with open("../inputs/day_16.txt") as infile:
        data = parse(infile.read().strip())

    _, part1, part2 = bits(data)
    print(part1)
    print(part2)
