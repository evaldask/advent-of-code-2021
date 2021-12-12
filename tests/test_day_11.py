from advent2021 import day_11


def data():
    return """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")


def test_parse():
    parsed = day_11.parse(data())

    assert [5, 4, 8, 3, 1, 4, 3, 2, 2, 3] == parsed[0]
    assert [5, 2, 8, 3, 7, 5, 1, 5, 2, 6] == parsed[-1]


def test_flash_count():
    parsed = day_11.parse(data())
    result = day_11.count_flashes(parsed, 10)

    assert 204 == result

    result = day_11.count_flashes(parsed, 100)
    assert 1656 == result


def test_sync_flash():
    parsed = day_11.parse(data())

    result = day_11.sync_flashes(parsed, 1000)
    assert 195 == result
