import pytest

from pytestSample.BaseClass import BaseClass


@pytest.mark.usefixtures("check")
class TestExample2(BaseClass):
    def test_createProfile(self, check):
        log = self.getLogger()
        log.info(check)
        log.info(check[1])
        print(check[1])