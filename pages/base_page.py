from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys


class BasePage:
    URL = 'https://b2c.passport.rt.ru'

    def __init__(self, browser):
        self.driver = browser

    def open_page(self):
        self.driver.get(self.URL)

    def find_element(self, locator, wait=0):
        try:
            if wait:
                return WebDriverWait(self.driver, wait).until(ec.presence_of_element_located(locator))
            else:
                return self.driver.find_element(*locator)
        except (TimeoutException, NoSuchElementException):
            return None

    def find_elements(self, locator, wait=0):
        try:
            if wait:
                return WebDriverWait(self.driver, wait).until(ec.presence_of_all_elements_located(locator))
            else:
                return self.driver.find_elements(*locator)
        except (TimeoutException, NoSuchElementException):
            return None

    @staticmethod
    def clear_field(field_element):
        if field_element.get_attribute('value'):
            field_element.clear()
        if field_element.get_attribute('value'):    # in case when clear method did not work
            field_element.click()
            field_element.send_keys(Keys.END)
            field_element.send_keys(Keys.LEFT_SHIFT, Keys.HOME)
            field_element.send_keys(Keys.DELETE)
