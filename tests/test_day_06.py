from advent2021 import day_06


def data():
    return [3, 4, 3, 1, 2]


def test_simulate():
    result = day_06.simulate(data(), 18)
    assert 26 == result

    result = day_06.simulate(data(), 80)
    assert 5934 == result

    result = day_06.simulate(data(), 256)
    assert 26984457539 == result
