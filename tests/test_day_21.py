from advent2021 import day_21


def test_play():
    result = day_21.play([4, 8])
    assert 739785 == result


def test_play2():
    result = day_21.dirac(4, 8)
    assert 444356092776315 == result
