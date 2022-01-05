from advent2021 import day_25


def data():
    return """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>""".split("\n")


def test_move():
    result = day_25.move(day_25.parse(data()))
    assert 58 == result
