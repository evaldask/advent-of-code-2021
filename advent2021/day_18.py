from typing import List, Union


DTYPE = List[Union[str, int]]


def parse(data: str) -> DTYPE:
    result: List[Union[str, int]] = []
    prev = None
    for symbol in data.strip():
        if symbol in ["[", ",", "]"]:
            if prev is not None:
                result.append(prev)
                prev = None
            result.append(symbol)

        else:
            number = int(symbol)
            if prev is not None:
                number = prev * 10 + number

            prev = number

    return result


def explode(data: DTYPE, max_depth: int = 4) -> DTYPE:
    depth = 0
    carry: int = 0
    prev = -1
    symbol = {"[": 1, "]": -1, ",": 0}
    result: DTYPE = []
    used = False
    skips = 0

    for i, item in enumerate(data):
        if skips > 0:
            skips -= 1
            continue
        if isinstance(item, str):
            depth += symbol[item]
            result.append(item)
            continue

        if depth > max_depth and not used:
            if data[i - 1] == "[":
                if prev >= 0:
                    result[prev] += item  # type: ignore
                result.pop()
                result.append(0)
                skips = 3
                carry = data[i + 2]  # type: ignore
                used = True

        else:
            if carry > 0:
                result.append(item + carry)
                carry = 0
                used = True
            else:
                result.append(item)
            prev = i

    return result


def split(data: DTYPE) -> DTYPE:
    for i, item in enumerate(data):
        if isinstance(item, int) and item > 9:
            return data[:i] + ["[", item // 2, ",", item - item // 2, "]"] + data[i+1:]
    return data


def sumup(left: DTYPE, right: DTYPE) -> DTYPE:
    pair: DTYPE = ["["] + left + [","] + right + ["]"]  # type: ignore

    for _ in range(1_000_000):
        original = stringify(pair)
        pair = explode(pair)
        exploded = stringify(pair)
        if original != exploded:
            continue

        pair = split(pair)
        splitted = stringify(pair)
        if splitted == original:
            return pair

    return [-1]


def stringify(data: DTYPE) -> str:
    return "".join([str(x) if isinstance(x, int) else x for x in data])


def magnitude(data: DTYPE) -> int:
    stack: List[int] = []
    for item in data:
        if item in ["[", ","]:
            continue

        if item == "]":
            right = stack.pop()
            left = stack.pop()

            stack.append(left * 3 + right * 2)  # type: ignore
        else:
            stack.append(item)  # type: ignore

    return sum(stack)


def largest_magnitude(data: List[DTYPE]) -> int:
    magnitudes = []
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j:
                continue
            magnitudes.append(magnitude(sumup(data[i], data[j])))

    return max(magnitudes)


if __name__ == "__main__":
    with open("../inputs/day_18.txt") as infile:
        data = infile.readlines()

    parsed = [parse(x) for x in data]
    result = parsed[0]
    for row in parsed[1:]:
        result = sumup(result, row)

    print(magnitude(result))
    print(largest_magnitude(parsed))
