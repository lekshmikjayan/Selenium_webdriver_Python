import pytest


@pytest.fixture(scope="class")
def verify():
    print("1 kwnfke")
    yield
    print("10 jhjewfkf")


@pytest.fixture()
def check():
    print("Creating user profile")
    return ["Lekshmi", "K Jayan", "www.elephant.com"]


@pytest.fixture(params=[("13","apples", "sold"),("25","oranges"),("244","grapes")])
def crossCheck(request):
    return request.param

