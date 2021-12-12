from advent2021 import day_12


def data():
    return """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".split("\n")


def data2():
    return """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".split("\n")


def test_parse():
    parsed = day_12.parse(data())

    assert "end" in parsed.get("A")
    assert "start" not in parsed.get("d")


def test_viable_routes():
    parsed = day_12.parse(data())
    result = day_12.viable_routes(parsed, 1)

    assert 10 == result


def test_viable_routes2():
    parsed = day_12.parse(data())
    result = day_12.viable_routes(parsed, 2)

    assert 36 == result

    parsed = day_12.parse(data2())
    result = day_12.viable_routes(parsed, 2, True)

    assert 103 == result
