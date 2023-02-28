import pytest

from pytestsDemo.baseClass import baseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(baseClass):

    def test_editprofile(self, dataLoad):
        log = self.getLogger()

        log.info(dataLoad[0])
        log.info(dataLoad[1])
        print(dataLoad[1])

