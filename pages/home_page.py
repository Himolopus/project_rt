from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    # locators
    LOGOUT_BUTTON = (By.ID, 'logout-btn')
    INFO_CARD = (By.CLASS_NAME, 'home__info-card')

    @property
    def logout_button(self):
        return self.find_element(self.LOGOUT_BUTTON, 3)

    @property
    def info_card(self):
        return self.find_element(self.INFO_CARD, 3)