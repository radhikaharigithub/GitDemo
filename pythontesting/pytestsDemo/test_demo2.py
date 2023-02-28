import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram(setup):
    msg = "Hello"
    assert msg == "Hi", "Test Failed"


def test_secondprogram():
    a = 4
    b = 6

    assert a+2 == 6, "addition do not match"


    