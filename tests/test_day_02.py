from advent2021 import day_02


def data():
    return """forward 5
down 5
forward 8
up 3
down 8
forward 2""".split("\n")


def test_problem2_parse():
    parsed = day_02.parse(data())

    assert parsed[0] == ("forward", 5)
    assert parsed[-1] == ("forward", 2)


def test_problem2_postion():
    parsed = day_02.parse(data())
    pos = day_02.position(parsed)

    assert 150 == pos


def test_problem2_aim():
    parsed = day_02.parse(data())
    pos = day_02.aim(parsed)

    assert 900 == pos
