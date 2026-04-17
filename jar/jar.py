
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self._capacity or self._size + n > self._capacity:
            raise ValueError("Over capacity")
        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not Enough Cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self, size):
        return self._size

jar = Jar()
jar.deposit(5)
jar.withdraw(3)

print(jar)

if __name__ == "__main__":
    main()
