import pytest


def test_pqr():
    s = 45
    b = 23
    assert b + 22 == s, 'yes, it is..'

@pytest.mark.usefixtures("verify")
class TestExample1:

    def test_fixtDemo7(self):
        print("executing steps in this 7 method")

    def test_fixtDemo9(self):
        print("executing steps in this 9 method")

    def test_fixtDemo8(self):
        print("executing steps in this 8 method")
