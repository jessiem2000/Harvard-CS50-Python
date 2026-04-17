from fuel import gauge, convert
import pytest


def test_convert():
    assert convert("3/4") == 75.0
    assert gauge(1.0) == "E"
    assert gauge(99.0) == "F"
    assert gauge(50) == "50%"


def test_valzero():
    with pytest.raises(ValueError):
        assert convert("-1/100")
    with pytest.raises(ZeroDivisionError):
        assert convert("50/0")


if __name__ == "__main__":
    main()
