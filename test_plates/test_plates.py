from plates import is_valid

def main():
    is_valid()

def test_plates_numberplacement():
    assert is_valid("cs50") == True
    assert is_valid("cs05") == False
    assert is_valid("cs50P") == False

def test_punc():
    assert is_valid("PI3.14") == False
    assert is_valid("cs$0?") == False

def test_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False

def test_zero():
    assert is_valid("tw5350") == True
    assert is_valid("tw0550") == False
    assert is_valid("cs50P") == False

def test_beginalpha():
    assert is_valid("24E3E") == False
    assert is_valid("adw50") == True
    assert is_valid("23asdw") == False
    assert is_valid("234a") == False
    assert is_valid("23") == False


def test_hasalpha():
    assert is_valid("cs50") == True
    assert is_valid("csasd5") == True
    assert is_valid("cs") == True

if __name__ == "__main__":
    main()
