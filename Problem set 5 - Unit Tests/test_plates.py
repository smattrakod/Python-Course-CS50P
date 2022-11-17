from plates import is_valid


def main():
    123
    # test_is_valid_numbers()
    # test_is_valid_punctuations()
    # test_is_valid_letter_end()
    # test_is_valid_nr_beginning()


def test_is_valid_numbers():
    assert is_valid("123344") == False
    assert is_valid("12334421") == False
    assert is_valid("123") == False
    assert is_valid("as344") == True
    assert is_valid("-12345") == False


def test_is_valid_punctuations():
    assert is_valid("as.123") == False
    assert is_valid("as 12 2") == False
    assert is_valid(" as2.4") == False
    assert is_valid("......") == False
    assert is_valid("1-1-32") == False
    assert is_valid("ga1231") == True


def test_is_valid_letter_end():
    assert is_valid("as123a") == False
    assert is_valid("as41AA") == False
    assert is_valid("aas2a1") == False
    assert is_valid("aas211") == True
    assert is_valid("CS5000") == True


def test_is_valid_nr_beginning():
    assert is_valid("50CS50") == False
    assert is_valid("1CS50") == False
    assert is_valid("12cs110") == False
    assert is_valid("False1") == True


if __name__ == "__main__":
    main()
