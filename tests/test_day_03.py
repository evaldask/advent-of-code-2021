from advent2021 import day_03


def data():
    return """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")


def test_problem3_parse():
    parsed = day_03.parse(data())

    assert [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0] == parsed[0]
    assert [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0] == parsed[-1]


def test_problem3_gamma_epsilon():
    parsed = day_03.parse(data())
    result = day_03.gamma_epsilon(parsed)

    assert 198 == result


def test_problem3_oxygen():
    parsed = day_03.parse(data())
    result = day_03.oxygen(parsed)

    assert 230 == result
