import pytest


@pytest.fixture()
def first_fixture():
    print("first fixture")
    return 1, 2, 3
