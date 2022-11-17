from bank import greeting


def main():
    test_hello()
    test_h()
    test_else()


def test_hello():
    assert greeting("hello, I'm fine") == "$0"
    assert greeting("hello, I'm fine! how about u?") == "$0"
    assert greeting("hellohellohello!") == "$0"
    assert greeting("hello, hello!") == "$0"


def test_h():
    assert greeting("hallelujah!") == "$20"
    assert greeting("hey there!") == "$20"
    assert greeting("having a good time") == "$20"
    assert greeting("hey ho!") == "$20"


def test_else():
    assert greeting("moneyyy!!! $100000") == "$100"
    assert greeting("1234") == "$100"
    assert greeting("well hello there!") == "$100"
    assert greeting("whey, hello hello hello") == "$100"
