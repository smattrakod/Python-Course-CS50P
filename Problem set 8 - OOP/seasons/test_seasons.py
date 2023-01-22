from seasons.seasons import check_input
import pytest


def main():
    test_check_input()


def test_check_input():
    assert check_input("1998-3-17") == (1998, 3, 17)
    assert check_input("1998-03-17") == (1998, 3, 17)
    with pytest.raises(SystemExit):
        check_input("1998-September-17")


if __name__ == "__main__":
    main()
