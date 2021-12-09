from advent2021 import day_05


def data():
    return """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""".split("\n")


def test_parse():
    parsed = day_05.parse(data())
    assert ((0, 9), (5, 9)) == parsed[0]
    assert ((5, 5), (8, 2)) == parsed[-1]


def test_vents():
    parsed = day_05.parse(data())
    result = day_05.vents_map(parsed)

    assert 5 == result


def test_diagonal():
    parsed = day_05.parse(data())
    result = day_05.diagonal(parsed)

    assert 12 == result
