from typing import Iterable, List, Tuple


def analize(data: List[str]) -> Iterable[Tuple[List[int], int]]:
    opening = ["(", "[", "{", "<"]
    closing = [")", "]", "}", ">"]

    for row in data:
        stack = []
        good = True
        for item in row.strip():
            if item in opening:
                stack.append(opening.index(item))
                continue

            idx = closing.index(item)

            if stack[-1] == idx:
                stack.pop()

            else:
                yield stack, idx
                good = False
                break

        if good:
            yield stack, -1


def error(data: List[str]) -> int:
    scores = [3, 57, 1197, 25137]
    result = 0

    for _, index in analize(data):
        if index >= 0:
            result += scores[index]

    return result


def complete(data: List[str]) -> int:
    scores = [1, 2, 3, 4]
    results = []

    for stack, index in analize(data):
        if index >= 0:
            continue

        result = 0
        rev = stack[::-1]
        for idx in rev:
            result = result * 5 + scores[idx]

        results.append(result)

    return sorted(results)[len(results) // 2]


if __name__ == "__main__":
    with open("../inputs/day_10.txt") as infile:
        data = infile.readlines()

    print(error(data))
    print(complete(data))
