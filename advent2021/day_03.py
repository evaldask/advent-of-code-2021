from typing import List


def parse(data: List[str]) -> List[List[int]]:
    results: List[List[int]] = []

    for line in data:
        for i, item in enumerate(line.strip()):
            if len(results) < i + 1:
                results.append([])

            results[i].append(int(item))

    return results


def gamma_epsilon(data: List[List[int]]) -> int:
    gamma = 0
    epsilon = 0
    lenght = len(data)

    for i, row in enumerate(data):
        total = sum(row)
        above = total > len(row) // 2
        power = pow(2, lenght - i - 1)
        gamma += power * above
        epsilon += power * (not above)

    return gamma * epsilon


def oxygen(data: List[List[int]]) -> int:
    def count(row, mask):
        res = {0: [], 1: []}
        for i in mask:
            res[row[i]].append(i)
        return res

    def preference(filtered, strategy):
        if strategy == "oxygen":
            return filtered[1] if len(filtered[1]) >= len(filtered[0]) else filtered[0]
        return filtered[0] if len(filtered[0]) <= len(filtered[1]) else filtered[1]

    def fmt(index):
        return int("".join([str(row[index]) for row in data]), 2)

    oxygen = 0
    co2 = 0

    oxygen_check = [i for i in range(len(data[0]))]
    co2_check = [i for i in range(len(data[0]))]

    for row in data:
        oxygen_check = preference(count(row, oxygen_check), "oxygen")
        if len(oxygen_check) == 1:
            oxygen = fmt(oxygen_check[0])
            oxygen_check = []

        co2_check = preference(count(row, co2_check), "co2")
        if len(co2_check) == 1:
            co2 = fmt(co2_check[0])
            co2_check = []

    return oxygen * co2


if __name__ == "__main__":
    with open("../inputs/day_03.txt") as infile:
        data = infile.readlines()

    parsed = parse(data)
    print(gamma_epsilon(parsed))
    print(oxygen(parsed))
