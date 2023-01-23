import pytest


@pytest.mark.smoke
@pytest.mark.skip

def test_abc():
    print("All izz well..!!!")

@pytest.mark.xfail
def test_gdgf():
    print("Do not display me...")


def test_crossCheck(crossCheck):
    print(crossCheck[1])

