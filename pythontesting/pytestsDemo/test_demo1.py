# py test file starts with test_ or _test
# method name also starts with test and code should be wrapped within method
# -k stands for method name execution
# -s logs in out put
# -v stands for more info metadata
# py.test <filename> - to run tests
# skip tests with @pytest.mark.skip
import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("hello")


@pytest.mark.xfail
def test_secondGreetCreditcard():
    print("Good Morning")


def test_fixtureDemo(setup):
    print("I will be execute steps in fixture demo method")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])



