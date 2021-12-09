from typing import List, Tuple


def won(board: List[int]) -> bool:
    pos = [x * 5 for x in range(5)]
    for i in range(5):
        if sum(board[i * 5: i * 5 + 5]) == 0:
            return True
        if sum([board[x + i] for x in pos]) == 0:
            return True

    return False


def parse(data: List[str]) -> Tuple[List[int], List[List[int]]]:
    draws = [int(x) for x in data[0].split(",")]

    data = data[2:]

    boards = []
    cells: List[int] = []

    for row in data:
        row = row.strip()

        if row == "":
            boards.append(cells)
            cells = []
            continue

        cells += [int(x) for x in row.split() if x != ""]

    if len(cells) > 0:
        boards.append(cells)

    return draws, boards


def last(draws: List[int], boards: List[List[int]]) -> int:
    solved = [False for _ in boards]

    for draw in draws:
        for i in range(len(boards)):
            if solved[i]:
                continue

            board = boards[i]
            if draw not in board:
                continue

            pos = board.index(draw)
            board[pos] = 0

            if won(board):
                solved[i] = True
                if all(solved):
                    return sum(board) * draw

            boards[i] = board

    return -1


def solve(draws: List[int], boards: List[List[int]]) -> int:
    for draw in draws:
        for i in range(len(boards)):
            board = boards[i]
            if draw not in board:
                continue

            pos = board.index(draw)
            board[pos] = 0

            if won(board):
                return sum(board) * draw

            boards[i] = board

    return -1


if __name__ == "__main__":
    with open("../inputs/day_04.txt") as infile:
        data = infile.readlines()

    draws, boards = parse(data)
    print(solve(draws, boards))
    print(last(draws, boards))
