from working.working import convert
import pytest


def main():
    test_convert_AM()
    test_convert_PM()
    test_convert_word()
    test_convert_not_AM_or_PM()
    test_convert_large()
    exit(0)


def test_convert_AM():
    assert convert("3 AM to 5 AM") == "03:00 to 05:00"
    assert convert("12 AM to 5 AM") == "00:00 to 05:00"
    assert convert("3:30 AM to 5 AM") == "03:30 to 05:00"
    assert convert("3:33 AM to 5:21 AM") == "03:33 to 05:21"


def test_convert_PM():
    assert convert("3 PM to 5 PM") == "15:00 to 17:00"
    assert convert("7 PM to 8:20 PM") == "19:00 to 20:20"
    assert convert("5 PM to 5:32 PM") == "17:00 to 17:32"
    assert convert("4 PM to 5 PM") == "16:00 to 17:00"


def test_convert_word():
    with pytest.raises(ValueError):
        convert("cat PM to 5 PM")


def test_convert_not_AM_or_PM():
    with pytest.raises(ValueError):
        convert("5 AM to 5 PM")


def test_convert_large():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


if __name__ == "__main__":
    main()
