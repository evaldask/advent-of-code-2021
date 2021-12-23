from advent2021 import day_23


def data():
    return """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########""".split()


def test_parse():
    room_map = day_23.parse(data())
    assert [".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."] == room_map[0]
    assert ["#", "#", "B", "#", "C", "#", "B", "#", "D", "#", "#"] == room_map[1]
    assert ["#", "#", "A", "#", "D", "#", "C", "#", "A", "#", "#"] == room_map[2]


def test_enc_dec():
    room_map = day_23.parse(data())
    decoded = day_23.dec(day_23.enc(room_map))

    assert room_map == decoded


def test_solution():
    room_map = day_23.parse(data())
    for x, y in zip(range(2, 10, 2), "ABCD"):
        room_map[1][x] = y
        room_map[2][x] = y

    result = day_23.solved(day_23.enc(room_map))

    assert result is True


def test_simulate():
    room_map = [list(".A.B...A..."), list("##B#C#B#D##"), list("##.#.#.#.##")]
    moves = day_23.simulate(day_23.enc(room_map), "B", 0, 3)
    possible = len(moves)
    assert 4 == possible


def test_available_moves():
    room_map = day_23.enc([list(".A.....A..."), list("##B########"), list("##.#.#.#.##")])
    result = [x for x in day_23.available_moves(room_map)]
    possible = len(result)
    costs = [x[1] for x in result]
    assert 9 == possible
    assert [1, 2, 4, 2, 4, 2, 3, 20, 40] == costs


def test_solve():
    room_map = day_23.parse(data())
    energy = day_23.solve(day_23.enc(room_map))
    assert 12521 == energy
