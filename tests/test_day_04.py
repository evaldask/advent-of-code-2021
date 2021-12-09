from advent2021 import day_04


def data():
    return """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")


def test_parse():
    draws, boards = day_04.parse(data())

    assert [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1] == draws
    assert [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19] == boards[0]
    assert [14, 21, 17, 24, 4, 10, 16, 15, 9, 19, 18, 8, 23, 26, 20, 22, 11, 13, 6, 5, 2, 0, 12, 3, 7] == boards[-1]


def test_winning():
    _, boards = day_04.parse(
        """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

 1 13 17 11  0
 0  2 23  4 24
 0  9 14 16  7
 0 10  3 18  5
 0 12 20 15 19""".split(
            "\n")
    )

    assert day_04.won(boards[0]) is False
    boards[0][0] = 0
    assert day_04.won(boards[0]) is True

    _, boards = day_04.parse(data())
    assert day_04.won(boards[-1]) is False
    for i in range(6):
        boards[-1][-i] = 0

    print(boards[-1])
    assert day_04.won(boards[-1]) is True


def test_solving():
    draws, boards = day_04.parse(data())
    result = day_04.solve(draws, boards)

    assert 4512 == result


def test_last_board():
    draws, boards = day_04.parse(data())
    result = day_04.last(draws, boards)

    assert 1924 == result
