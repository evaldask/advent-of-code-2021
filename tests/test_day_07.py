from advent2021 import day_07


def test_fuel_spent():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = day_07.fuel_spent(data, day_07.part1)

    assert 37 == result


def test_fuel_spent2():
    data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    result = day_07.fuel_spent(data, day_07.part2)

    assert 168 == result
