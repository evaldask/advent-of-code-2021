from advent2021 import day_09


def data():
    return """2199943210
3987894921
9856789892
8767896789
9899965678""".split("\n")


def test_parse():
    parsed = day_09.parse(data())

    assert [2, 1, 9, 9, 9, 4, 3, 2, 1, 0] == parsed[0]
    assert [9, 8, 9, 9, 9, 6, 5, 6, 7, 8] == parsed[-1]


def test_low_points():
    parsed = day_09.parse(data())
    result = day_09.low_points(parsed)

    assert 15 == result


def test_basins():
    parsed = day_09.parse(data())
    result = day_09.basins(parsed)

    assert 1134 == result
