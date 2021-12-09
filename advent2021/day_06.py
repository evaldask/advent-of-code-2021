from collections import defaultdict


def simulate(fishes, days):
    fish_dict = defaultdict(lambda: 0)
    for fish in fishes:
        fish_dict[fish] += 1

    for _ in range(days):
        next_day = defaultdict(lambda: 0)
        for day, count in fish_dict.items():
            day -= 1

            if day >= 0:
                next_day[day] += count
                continue

            next_day[6] += count
            next_day[8] += count

        fish_dict = next_day

    return sum([x for x in fish_dict.values()])


if __name__ == "__main__":
    data = []
    with open("../inputs/day_06.txt") as infile:
        for line in infile:
            data.append(int(line.strip()))

    print(simulate(data, 80))
    print(simulate(data, 256))
