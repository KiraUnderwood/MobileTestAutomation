from appium.webdriver.common.touch_action import TouchAction


class Calculator:
    class Locators:
        top_toolbar_id = 'com.google.android.calculator:id/toolbar'
        slide_bar_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.slidingpanelayout.widget.SlidingPaneLayout'
        five_id = 'com.google.android.calculator:id/digit_5'
        four_id = 'com.google.android.calculator:id/digit_4'
        cos_id = 'com.google.android.calculator:id/fun_cos'
        eq_id = 'com.google.android.calculator:id/eq'
        result_id = 'com.google.android.calculator:id/result_preview'
        mult_id = 'com.google.android.calculator:id/op_mul'
        slide_close_id = 'com.google.android.calculator:id/arrow'
        formula_field_id = 'com.google.android.calculator:id/formula'

    def __init__(self, driver):
        self.driver = driver
        self.locators = self.Locators()

    def unfold_slider(self):
        boundary = 10
        slider_element = self.driver.find_element_by_xpath(self.Locators.slide_bar_xpath)
        four_element = self.driver.find_element_by_id(self.Locators.four_id)
        slider = slider_element.location
        slider_wh = slider_element.size
        four = four_element.location
        pressX = slider['x']+slider_wh['width'] - boundary
        pressY = slider['y']+slider_wh['height']/2
        TouchAction(self.driver).press(x=pressX, y=pressY).move_to(x=four['x'], y=four['y']).release().perform()

    def fold_slider(self):
        self.driver.find_element_by_id(self.Locators.slide_close_id).click()
