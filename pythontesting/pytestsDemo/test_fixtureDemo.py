import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will be execute steps in fixturedemo method")

    def test_fixtureDemo1(self):
        print("I will be execute steps in fixturedemo1 method")

    def test_fixtureDemo2(self):
        print("I will be execute steps in fixturedemo2 method")

    def test_fixtureDemo3(self):
        print("I will be execute steps in fixturedemo3 method")


