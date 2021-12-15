from advent2021 import day_15


def data():
    return """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581""".split("\n")


def test_navigate():
    parsed = day_15.parse(data())
    map_data = day_15.Map(parsed, 1)
    result = day_15.navigate(map_data)

    assert 40 == result


def test_navigate_scaled():
    parsed = day_15.parse(data())
    map_data = day_15.Map(parsed, 5)
    result = day_15.navigate(map_data)

    assert 315 == result
