from advent2021 import day_18


def test_split():
    parsed = day_18.parse("[[[[0,7],4],[15,[0,13]]],[1,1]]")
    result = day_18.split(parsed)
    assert "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]" == day_18.stringify(result)

    result = day_18.split(result)
    assert "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]" == day_18.stringify(result)


def test_explode():
    parsed = day_18.parse("[[[[[9,8],1],2],3],4]")
    result = day_18.explode(parsed)
    assert "[[[[0,9],2],3],4]" == day_18.stringify(result)

    parsed = day_18.parse("[[6,[5,[4,[3,2]]]],1]")
    result = day_18.explode(parsed)
    assert "[[6,[5,[7,0]]],3]" == day_18.stringify(result)

    parsed = day_18.parse("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
    result = day_18.explode(parsed)
    assert "[[3,[2,[8,0]]],[9,[5,[7,0]]]]" == day_18.stringify(result)

    parsed = day_18.parse("[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]")
    result = day_18.explode(parsed)
    assert "[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]" == day_18.stringify(result)


def test_sumup():
    left = day_18.parse("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]")
    right = day_18.parse("[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]")
    result = day_18.sumup(left, right)
    assert "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]" == day_18.stringify(result)


def test_homework():
    data = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]""".split("\n")

    data = [day_18.parse(x) for x in data]

    result = data[0]
    for row in data[1:]:
        result = day_18.sumup(result, row)

    assert "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]" == day_18.stringify(result)

    result = day_18.magnitude(result)
    assert 4140 == result

    result = day_18.largest_magnitude(data)
    assert 3993 == result
