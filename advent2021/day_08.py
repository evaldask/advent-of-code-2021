from typing import List, Tuple

DATA_TYPE = List[Tuple[List[str], List[str]]]


def parse(data: List[str]) -> DATA_TYPE:
    results = []
    for row in data:
        splitted = row.strip().split(" | ")
        assert 2 == len(splitted)

        results.append((splitted[0].split(" "), splitted[1].split(" ")))

    return results


def count(data: DATA_TYPE) -> int:
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    result = 0

    for _, output in data:
        for out in output:
            size = len(out)
            if size in segments and segments.index(size) in [1, 4, 7, 8]:
                result += 1

    return result


def sumup(data: DATA_TYPE) -> int:
    result = 0
    segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for indata, output in data:
        results = {}
        for known in [1, 7, 4, 8]:
            filtered = [x for x in indata if len(x) == segments[known]]
            assert len(filtered) == 1
            results[known] = set(filtered[0])

        sets = [set(x) for x in indata]
        results[9] = [x for x in sets if len(x) == 6 and x.issuperset(results[4])][0]
        results[0] = [x for x in sets if len(x) == 6 and x.issuperset(results[1]) and not x.issuperset(results[4])][0]
        results[6] = [x for x in sets if len(x) == 6 and x != results[0] and x != results[9]][0]
        results[5] = [x for x in sets if len(x) == 5 and x.issubset(results[6])][0]
        results[2] = [x for x in sets if len(x) == 5 and results[5] | x == results[8]][0]
        results[3] = [x for x in sets if len(x) == 5 and x != results[2] and x != results[5]][0]

        partial = 0
        for out in output:
            for k, v in results.items():
                if set(out) == v:
                    partial = partial * 10 + k

        result += partial

    return result


if __name__ == "__main__":
    with open("../inputs/day_08.txt") as infile:
        data = infile.readlines()

    coords = parse(data)
    print(count(coords))
    print(sumup(coords))
