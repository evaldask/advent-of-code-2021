from collections import Counter
from typing import List
from typing import Counter as TypedCounter


def polymer(steps: int, template: str, rules: List[str]) -> int:
    rules_dict = {}
    for rule in rules:
        key, value = rule.strip().split(" -> ")
        rules_dict[key] = value

    pairs: TypedCounter[str] = Counter([x + y for x, y in zip(template, template[1:])])

    for _ in range(steps):
        new_pairs: TypedCounter[str] = Counter()

        for key, value in pairs.items():  # type: ignore
            symbol = rules_dict[key]
            new_pairs[key[0] + symbol] += value  # type: ignore
            new_pairs[symbol + key[1]] += value  # type: ignore

        pairs = new_pairs

    counts = []
    for symbol in set("".join(pairs.keys())):
        first = sum([v for k, v in pairs.items() if k[0] == symbol])
        second = sum([v for k, v in pairs.items() if k[1] == symbol])
        counts.append(max(first, second))

    return max(counts) - min(counts)


if __name__ == "__main__":
    with open("../inputs/day_14.txt") as infile:
        data = infile.readlines()

    print(polymer(10, data[0].strip(), data[2:]))
    print(polymer(40, data[0].strip(), data[2:]))
