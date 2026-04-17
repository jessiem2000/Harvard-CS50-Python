from bank import value

def main():
    value()

def test_value():
    assert value("hello") == 0
    assert value("Hiya") == 20

def test_casevalue():
    assert value("HELLO") == 0
    assert value("HIYA") == 20

def test_entirevalue():
    assert value("How are you?") == 20
    assert value("what's up?") == 100


if __name__ == "__main__":
    main()
