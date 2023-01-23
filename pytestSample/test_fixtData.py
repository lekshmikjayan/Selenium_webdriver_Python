import pytest


@pytest.mark.usefixtures("check")
class TestExample2:
    def test_createProfile(self, check):
        print(check)
        print(check[1])