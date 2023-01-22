import pytest
from project import readcsv
from project import check_file
from project import total_rev


revenue_list = [['computer', 780.0], ['earphones', 270.0], ['calculator', 260.0], ['whisky', 60.0], ['vodka', 48.0],    ['fish', 26.0], ['meatballs', 25.0], ['shampoo', 13.0], ['beer', 9.1], ['deodorant', 7.5], [
    'ice-cream', 7.0], ['redbull', 6.0], ['pineapple', 6.0], ['eggs', 5.6000000000000005], ['coca-cola', 5.5], ['cookies', 5.0], ['banana', 4.8], ['fanta', 4.5], ['pasta', 4.0], ['candy', 4.0], ['apple', 2.8000000000000003], ['chips', 2.4]]

revenue_list2 = [["apple", 30.0], ["redbull", 40.0], ["chips", 30.0]]


def test_readcsv():
    with pytest.raises(SystemExit):
        readcsv("CS50.csv")
    with pytest.raises(SystemExit):
        readcsv("saales.csv")


def test_check_file():
    with pytest.raises(SystemExit):
        check_file("hello.txt")


def test_total_rev():
    assert total_rev(revenue_list) == '1556.2'
    assert total_rev(revenue_list2) == '100.0'
