from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar._size == 1
    jar.deposit(5)
    assert jar._size == 6

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar._size == 5

if __name__ == "__main__":
    main()
