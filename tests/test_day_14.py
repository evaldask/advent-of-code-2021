from advent2021 import day_14


def data():
    return """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".split("\n")


def test_polymer():
    value = data()
    template = value[0]
    rules = value[2:]

    result = day_14.polymer(10, template, rules)
    assert 1588 == result
