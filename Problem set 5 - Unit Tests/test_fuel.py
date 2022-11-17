import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("5/10") == 50
    assert convert("5/10") == 50
    assert convert("5/10") == 50


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(77) == "77%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
