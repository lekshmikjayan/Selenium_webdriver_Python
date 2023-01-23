import pytest


@pytest.mark.smoke
def test_check():
    msg = "hello"
    assert msg == "Hi","wrong msg passed"

def test_Sample2():
    a = 17
    b = 9
    assert a == b +8, "correct"

