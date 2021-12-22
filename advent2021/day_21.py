from functools import lru_cache
from collections import Counter
from itertools import cycle, product

from typing import List
from typing import Counter as TypedCounter


def position(pos: int, roll: int) -> int:
    return (pos + roll - 1) % 10 + 1


def dice(lower: int = 1, upper: int = 100):
    items = list(range(lower, upper + 1))
    for item in cycle(items):
        yield item


def play(players: List[int]) -> int:
    scores = [0 for _ in players]
    dice_rolls = 0
    rolling_dice = dice()

    for _ in range(1_000_000):
        for i in range(len(players)):
            rolled = next(rolling_dice) + next(rolling_dice) + next(rolling_dice)
            dice_rolls += 3

            players[i] = position(players[i], rolled)
            scores[i] += players[i]

            if scores[i] >= 1000:
                return scores[i - 1] * (dice_rolls)

    return -1


def dirac(player1: int, player2: int) -> int:
    @lru_cache(maxsize=1_000_000)
    def play(pos1: int, pos2: int, score1: int, score2: int, p1: int):
        if score2 >= 21:
            return Counter([p1])

        counter: TypedCounter[int] = Counter()
        for roll in all_rolls:
            pos = position(pos1, roll)
            outcome = play(pos2, pos, score2, score1 + pos, p1 * -1)
            counter += outcome

        return counter

    all_rolls = [sum(x) for x in product(range(1, 4), repeat=3)]
    result = play(player1, player2, 0, 0, 1)
    return result.most_common()[0][1]


if __name__ == "__main__":
    print(play([1, 6]))
    print(dirac(1, 6))
