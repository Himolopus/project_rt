from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PhoneEmailConfirmPage(BasePage):
    # locators
    TITLE = (By.CLASS_NAME, 'card-container__title')
    CODE_FIELD = (By.ID, 'rt-code-0')
    ERROR_MESSAGE = (By.ID, 'form-error-message')
    # expected text of elements
    PHONE_CONFIRM_TITLE = 'Подтверждение телефона'
    EMAIL_CONFIRM_TITLE = 'Подтверждение email'
    WRONG_CODE_ERROR = 'Неверный код. Повторите попытку'

    @property
    def title(self):
        self.find_element(self.CODE_FIELD, 10)
        return self.find_element(self.TITLE)

    @property
    def code_field(self):
        return self.find_element(self.CODE_FIELD, 10)

    @property
    def error_message(self):
        return self.find_element(self.ERROR_MESSAGE, 10)

    def enter_code(self, code):
        self.code_field.send_keys(code)
