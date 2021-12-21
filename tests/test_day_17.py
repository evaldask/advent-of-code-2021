from advent2021 import day_17


def test_parse():
    x, y = day_17.parse("target area: x=20..30, y=-10..-5")
    assert (20, 30) == x
    assert(-10, -5) == y


def test_velocity():
    result, options = day_17.trajectory((20, 30), (-10, -5))
    assert 45 == result
    assert 112 == options
