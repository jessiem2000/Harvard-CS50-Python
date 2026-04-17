from numb3rs import validate




def test_alpha():
    assert validate("cat") == False

def test_numeric():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("192.168.001.1") == False



if __name__ == "__main__":
    main()
