from twttr import shorten

vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def main():
    test_shorten()

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten("tw1tt3r") == "tw1tt3r"
    assert shorten ("TW1TT3R") == "TW1TT3R"

def test_punc():
    assert shorten("Do you use twitter?") == "D y s twttr?"
if __name__ == "__main__":
    main()
