from numb3rs import validate


def test_validate_large():
    assert validate("222.222.222.222") == True
    assert validate("222.31.41.234") == True
    assert validate("4123.1234.256.222") == False
    assert validate("275.222.222.222") == False
    assert validate("282.222.222.222") == False


def test_validate_negative():
    assert validate("-123.234.256.222") == False
    assert validate("-25.222.222.222") == False
    assert validate("-1.222.222.222") == False


def test_validate_special():
    assert validate("275:222.222.222") == False
    assert validate("282.222.222.222!") == False
    assert validate("282.222.222.222,") == False
    assert validate("282.222.222,222") == False


def test_validate_char():
    assert validate("275:222.2a.222") == False
    assert validate("282.B123.222.222!") == False
    assert validate("282.X.222.222,") == False
    assert validate("282.1a2.222,222") == False
