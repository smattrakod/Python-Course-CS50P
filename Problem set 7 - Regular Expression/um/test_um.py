from um import count


def test_count():
    assert count("ummu um uma umum um") == 2
    assert count("um uma umum um") == 2
    assert count("ummu um uma umum um um um") == 4
    assert count("ummu um uma um um um ") == 4


def test_punctuation():
    assert count("um. umma. um. um.") == 3
    assert count("um um.") == 2


def test_comma():
    assert count("um, umma, um,um, my name um, is viktor um, ") == 5
    assert count("um um,") == 2


def test_special():
    assert count("um, #asd um um@ a?!= um?") == 4
