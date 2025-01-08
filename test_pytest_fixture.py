import pytest


# pytest 在每个测试函数的外层会自动的把函数包装成一个测试类

def test_first_fixture(first_fixture):
    print("test_first_fixture")
    assert first_fixture == (1, 2, 3)


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("session_fixture")


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    print("module_fixture")


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    print("class_fixture")


test_data = [
    {
        "username": "1",
        "password": "123",
        "desc": "success"
    },
    {
        "username": "1",
        "password": "abc",
        "desc": "failed"
    },
    {
        "username": "2",
        "password": "123",
        "desc": "success"
    }
]

@pytest.fixture(params=test_data)
def param_data(request):
    return request.param

def test_login(param_data):
    print(param_data)

