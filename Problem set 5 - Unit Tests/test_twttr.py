from twttr import shorten
import twttr2


def main():
    test_shorten2()
    test_shorten()


def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("TwiTTER") == "TwTTR"
    assert shorten("12ER120 EER") == "12R120 R"
    assert shorten("-12aaaqweAA") == "-12qw"


def test_shorten2():
    assert twttr2.shorten("twIttEr") == "twttr"
    assert twttr2.shorten("TwITTER") == "TwTTR"
    assert twttr2.shorten("12ER120 EER") == "12R120 R"
    assert twttr2.shorten("-12aaaqwEAA") == "-12qw"


if __name__ == "__main__":
    main()
