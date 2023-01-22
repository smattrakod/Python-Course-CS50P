
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Negative Capacity Not OK")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return (self._size * "🍪")

    def deposit(self, n):
        if (n + self.size) > self.capacity:
            raise ValueError("Exceeding Capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not Enough Cookies in the Jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(100)
    # jar.size()
    jar.deposit(50)
    print(jar)
    jar.withdraw(49)
    print(jar)
