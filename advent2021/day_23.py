import heapq
from functools import lru_cache
from typing import List, Dict, Tuple, Generator


def parse(data: List[str]) -> List[List[str]]:
    hallway = []
    rooms = []
    for row in data:
        sub = row.strip().replace("#", "")

        if len(sub) == 0:
            continue

        if sub.startswith("."):
            hallway = list(sub)

        else:
            rooms.append(list(sub))

    room_map = [hallway]
    for room in rooms:
        floor = ["#"] * len(hallway)
        floor[2] = room[0]
        floor[4] = room[1]
        floor[6] = room[2]
        floor[8] = room[3]
        room_map.append(floor)

    return room_map


def costs(moves: int, amphipod: str) -> int:
    energy = {"A": 1, "B": 10, "C": 100, "D": 1000}
    return energy.get(amphipod, 1_000_000) * moves


def solved(room: str) -> bool:
    room_map = dec(room)

    for floor in room_map[1:]:
        for i, v in zip(range(2, 10, 2), "ABCD"):
            if floor[i] != v:
                return False

    return True


def enc(room_map: List[List[str]]) -> str:
    return "\n".join(["".join(x) for x in room_map])


def dec(room_map: str) -> List[List[str]]:
    return [list(x) for x in room_map.split("\n")]


@lru_cache(maxsize=None)
def simulate(room: str, amphipod: str, x: int, y: int, cost: int = 0) -> List[Tuple[int, int, int]]:
    indexes = {"A": 2, "B": 4, "C": 6, "D": 8}
    options = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    moves = []

    room_map = dec(room)

    for dx, dy in options:
        mx = x + dx
        my = y + dy
        if 0 <= mx < len(room_map) and 0 <= my < len(room_map[0]):
            if mx > 0 and my != indexes[amphipod] and x == 0:
                continue

            if room_map[mx][my] != ".":
                continue

            room_map[mx][my] = amphipod.lower()
            total_cost = costs(1, amphipod) + cost
            moves.append((mx, my, total_cost))
            moves += simulate(enc(room_map), amphipod, mx, my, total_cost)

    return moves


@lru_cache(maxsize=None)
def available_moves(room: str) -> Generator[Tuple, None, None]:
    amphipod_indexes = {l: p for l, p in zip("ABCD", range(2, 10, 2))}  # noqa: E741
    amphipod_positions = []

    room_map = dec(room)

    for x, row in enumerate(room_map):
        for y, value in enumerate(row):
            if value in "ABCD":
                amphipod_positions.append((value, x, y))

    for amphipod, x, y in amphipod_positions:
        for dx, dy, cost in simulate(room, amphipod, x, y):
            if (dx > 0 and dy != amphipod_indexes[amphipod]) or (dx == 0 and dy in [2, 4, 6, 8]):
                continue

            possible = dec(room)
            possible[x][y] = "."
            possible[dx][dy] = amphipod
            encoded = enc(possible)

            yield encoded, cost


def solve(room: str) -> int:
    costs: Dict[str, int] = {}
    to_visit = [(0, room)]

    while to_visit:
        spent, explore = heapq.heappop(to_visit)

        if solved(explore):
            return costs[explore]

        for possible_move, energy in available_moves(explore):
            if costs.get(possible_move, 1_000_000) < energy + spent:
                continue

            costs[possible_move] = energy + spent
            heapq.heappush(to_visit, (energy + spent, possible_move))

    return -1


if __name__ == "__main__":
    with open("../inputs/day_23.txt") as infile:
        data = infile.read()
        part1, part2 = data.split("\n\n")

    print(solve(enc(parse(part1.split("\n")))))
    # print(solve(enc(parse(part2.split("\n")))))
