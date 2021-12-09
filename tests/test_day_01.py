from advent2021 import day_01


def data():
    return """199
200
208
210
200
207
240
269
260
263""".split("\n")


def test_parse():
    parsed = day_01.parse(data())

    assert 199 == parsed[0]
    assert 263 == parsed[-1]


def test_increase1():
    parsed = day_01.parse(data())
    result = day_01.larger(parsed)

    assert 7 == result


def test_increase2():
    parsed = day_01.parse(data())
    result = day_01.larger3(parsed)

    assert 5 == result
