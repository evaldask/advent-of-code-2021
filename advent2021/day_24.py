from functools import lru_cache
from typing import Tuple, List, Optional


def number(row: str) -> int:
    return int(row.strip().split(" ")[-1])


def parse(data: List[str]) -> List[Tuple[int, int, int]]:
    res = []
    for i in range(0, len(data), 18):
        res.append((number(data[i + 4]), number(data[i + 5]), number(data[i + 15])))

    return res


def alu(data: List[Tuple[int, int, int]], maximum: bool) -> Optional[str]:
    if maximum:
        options = list(range(9, 0, -1))
    else:
        options = list(range(1, 10))

    @lru_cache(maxsize=1_000_000)
    def f(z: int, index: int) -> Optional[str]:
        if index == 14:
            return "" if z == 0 else None

        q, a, b = data[index]

        for w in options:
            zdiv = z // q
            if z % 26 == w - a:
                z_new = zdiv
            else:
                z_new = 26 * zdiv + w + b

            result = f(z_new, index + 1)

            if result is not None:
                return str(w) + result

        return None

    return f(0, 0)


if __name__ == "__main__":
    with open("../inputs/day_24.txt") as infile:
        data = infile.readlines()

    parsed = parse(data)
    print(alu(parsed, maximum=True))
    print(alu(parsed, maximum=False))
