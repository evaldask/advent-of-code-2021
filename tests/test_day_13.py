from advent2021 import day_13


def data():
    return """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".split("\n")


def test_parse():
    coords, folds = day_13.parse(data())

    assert (8, 4) in coords
    assert ("y", 7) in folds


def test_fold():
    coords, folds = day_13.parse(data())
    result = day_13.fold(coords, folds[:1])

    assert 17 == result
