from advent2021 import day_16


def test_bits():
    _, result, _ = day_16.bits(day_16.parse("8A004A801A8002F478"))
    assert 16 == result

    _, result, _ = day_16.bits(day_16.parse("620080001611562C8802118E34"))
    assert 12 == result

    _, result, _ = day_16.bits(day_16.parse("C0015000016115A2E0802F182340"))
    assert 23 == result

    _, result, _ = day_16.bits(day_16.parse("A0016C880162017C3686B18A3D4780"))
    assert 31 == result


def test_bits2():
    _, _, result = day_16.bits(day_16.parse("C200B40A82"))
    assert 3 == result

    _, _, result = day_16.bits(day_16.parse("04005AC33890"))
    assert 54 == result

    _, _, result = day_16.bits(day_16.parse("880086C3E88112"))
    assert 7 == result

    _, _, result = day_16.bits(day_16.parse("D8005AC2A8F0"))
    assert 1 == result

    _, _, result = day_16.bits(day_16.parse("CE00C43D881120"))
    assert 9 == result

    _, _, result = day_16.bits(day_16.parse("F600BC2D8F"))
    assert 0 == result

    _, _, result = day_16.bits(day_16.parse("9C005AC2F8F0"))
    assert 0 == result

    _, _, result = day_16.bits(day_16.parse("9C0141080250320F1802104A08"))
    assert 1 == result
