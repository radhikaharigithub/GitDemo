import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Radhika", "HG", "Student"]


@pytest.fixture(params=[("chrome", "Radhika", "Harish"), ("Firefox", "Aarush"), ("IE", "ss")])
def crossBrowser(request):
    return request.param

