import pytest

from selenium.webdriver.common.action_chains import ActionChains

from ConfigsForTests.CalculatorElements import Calculator

'''
Got this calculator apk for testing:
https://apkpure.com/calculator/com.google.android.calculator
and its elements locators are in CalculatorElements module

Found a bug in this one! In this App Cos is not correctly calculated and the test fails.
'''


class TestCasesNative:
    @pytest.fixture(scope="function")
    def view(self, driver_for_native):
        calc = Calculator(driver_for_native)
        yield calc

    @pytest.mark.parametrize("angle", [88])
    def test_calc_cos(self, view, angle):
        import math
        py_cos = round(math.cos(angle), 6)
        view.unfold_slider()

        actions = ActionChains(view.driver)
        actions.click(view.driver.find_element_by_id(view.Locators.cos_id))
        actions.pause(5)
        actions.send_keys_to_element(view.driver.find_element_by_id(view.Locators.formula_field_id), str(angle))
        actions.perform()

        res_elem = view.driver.find_element_by_id(view.Locators.result_id)
        cos_result = res_elem.get_attribute('text')
        cos_result_float = round(float(cos_result), 6)

        assert cos_result_float == py_cos, f"Cos calculated by python math module is {py_cos} and is not equal to the " \
                                           f"Cos calculated by the Android App {cos_result_float} "

