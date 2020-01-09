import pytest

from ConfigsForTests.BookingCom import Booking
'''
Chrome driver 61.0.3163.0 on Nexus 5X API 27
http://appium.io/docs/en/writing-running-appium/web/chromedriver/
and its elements locators are in BookingCom module
'''


class TestCasesWebSite:
    @pytest.fixture(scope="function")
    def view(self, driver_for_web):
        calc = Booking(driver_for_web)
        yield calc

    def test_login_to_account(self, view):
        view.set_destination(dest="Stockholm")
        number_of_results = view.get_results()
        assert number_of_results > 0




