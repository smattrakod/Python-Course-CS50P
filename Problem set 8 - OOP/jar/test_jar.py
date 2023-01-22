from jar import Jar
import pytest


def test_init():
    jar1 = Jar(5)
    assert jar1.capacity == 5
    assert jar1.size == 0
    jar2 = Jar()
    assert jar2.capacity == 12
    assert jar2.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.size == 5
    jar.withdraw(3)
    jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)
