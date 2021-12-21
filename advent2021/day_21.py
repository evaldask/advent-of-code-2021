from itertools import cycle
from functools import lru_cache
from collections import Counter
from typing import List
from typing import Counter as TypedCounter


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

            players[i] = (players[i] + rolled - 1) % 10 + 1
            scores[i] += players[i]

            if scores[i] >= 1000:
                return scores[i - 1] * (dice_rolls)

    return -1


def dirac(player1: int, player2: int) -> int:
    def dice_roll():
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    yield i + j + k

    def position(p, r): return (p + r - 1) % 10 + 1

    @lru_cache(maxsize=1_000_000)
    def play(pos1: int, pos2: int, score1: int, score2: int, player_1_moves: bool):
        if score1 >= 21:
            return Counter([1])

        if score2 >= 21:
            return Counter([-1])

        counter: TypedCounter[int] = Counter()
        if player_1_moves is True:
            for roll in all_rolls:
                pos = position(pos1, roll)
                outcome = play(pos, pos2, score1 + pos, score2, False)
                counter += outcome
        else:
            for roll in all_rolls:
                pos = position(pos2, roll)
                outcome = play(pos1, pos, score1, score2 + pos, True)
                counter += outcome

        return counter

    all_rolls = [x for x in dice_roll()]
    result = play(player1, player2, 0, 0, True)
    return result.most_common()[0][1]


if __name__ == "__main__":
    print(play([1, 6]))
    print(dirac(1, 6))
