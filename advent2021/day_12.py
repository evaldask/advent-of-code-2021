from collections import defaultdict
from typing import List, Dict


def parse(data: List[str]) -> Dict[str, List[str]]:
    paths = defaultdict(lambda: [])

    for row in data:
        splitted = row.strip().split("-")
        assert 2 == len(splitted)

        edge_a = splitted[0]
        edge_b = splitted[1]

        paths[edge_a].append(edge_b)
        paths[edge_b].append(edge_a)

    return paths


def route_filter(route, limit):
    if limit == 1:
        return True

    seen = {}
    for item in route:
        if item.isupper():
            continue

        if item in seen:
            return True

        seen[item] = True

    return False


def viable_routes(data: Dict[str, List[str]], limit: int, debug=False) -> int:
    routes = []

    def explore(position, route):
        if position == "end":
            routes.append(route + ["end"])
            return

        new_routes = route + [position]
        for option in data[position]:
            if option == "start":
                continue
            if option.islower() and option in route and route_filter(new_routes, limit):
                continue

            explore(option, new_routes)

    explore("start", [])
    return len(routes)


if __name__ == "__main__":
    with open("../inputs/day_12.txt") as infile:
        data = parse(infile.readlines())

    print(viable_routes(data, 1))
    print(viable_routes(data, 2))
