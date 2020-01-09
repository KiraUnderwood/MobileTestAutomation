from appium.webdriver.common.touch_action import TouchAction


class Booking:
    class Locators:
        desti_inp_id = 'input_destination'
        dest_xpath = '//android.app.Dialog[@content-desc="Enter destination"]/android.view.View[2]/android.view.View/android.view.View/android.widget.EditText'
        found_options_xpath = '//android.app.Dialog[@content-desc="Enter destination"]/android.view.View[2]/android.widget.ListView'
        cookies_aid = 'Accept'
        cookies_xpath = '//android.widget.Button[@content-desc="Accept"]'
        submit_search_id = 'submit_search'
        close_xpath = '(//android.widget.Button[@content-desc="Close"])[2]'
        field_xpath = '//android.app.Dialog[@content-desc="Select dates"]/android.view.View[3]'
        full_view_xpath = '//android.webkit.WebView[@content-desc="Booking.com | Official site | The best hotels & accommodations"]/android.view.View[5]/android.view.View/android.view.View[3]'
        form_search_location_id = 'form_search_location'
        results_xpath = "//android.view.View[contains(@content-desc,'results')]"  # in Appium desctop this locator works, but in test it does not, not sure why
        # "//*[@class = 'android.view.View' and contains(@content-desc,'results')]"

    def __init__(self, driver):
        self.driver = driver
        self.locators = self.Locators()

    def set_destination(self, dest: str):
        dest_element = self.driver.find_element_by_id(self.Locators.desti_inp_id)
        dest_element.send_keys(dest)
        dest_element.click()

        # could not find the coordinates to tap on based on teh element location
        '''
        dest_renewed = self.driver.find_element_by_xpath(self.Locators.dest_xpath)
        print(dest_renewed.location)
        print(dest_renewed.size)
        poinX = dest_renewed.location['x'] + dest_renewed.size['width'] / 2
        pointY =dest_renewed.location['y'] + dest_renewed.size['height'] / 2
        '''

        # tap on first result in a search
        pointX = 300
        pointY = 600
        TouchAction(self.driver).wait(3000).tap(x=pointX, y=pointY).perform()

        # tap to auto-agree on default dates
        _pointX = 450
        _pointY = 1680
        TouchAction(self.driver).wait(3000).tap(x=_pointX, y=_pointY).perform()

        # tap to accept cookies
        TouchAction(self.driver).wait(3000).tap(x=_pointX, y=_pointY).perform()

        # scroll to the Submit button
        slide_from_x = 1034
        slide_from_y = 1230
        slide_to_x = 984
        slide_to_y = 409
        TouchAction(self.driver).wait(3000).press(x=slide_from_x, y=slide_from_y).move_to(x=slide_to_x,
                                                                                          y=slide_to_y).release().perform()
        # click on submit
        self.driver.find_element_by_id(self.Locators.submit_search_id).click()

    def get_results(self):
        results = self.driver.find_element_by_xpath(self.Locators.results_xpath)
        import re
        number_of_results = re.findall(r'\d+', results.get_attribute('content-desc'))
        if number_of_results:
            return int(number_of_results[0])
