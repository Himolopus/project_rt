from pages.base_page import BasePage
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
from random import randint


class RegistrationPage(BasePage):
    # locators
    LEFT_BLOCK = (By.ID, 'page-left')
    RIGHT_BLOCK = (By.ID, 'page-right')
    TITLE = (By.CLASS_NAME, 'card-container__title')
    FIRSTNAME_FIELD = (By.NAME, 'firstName')
    LASTNAME_FIELD = (By.NAME, 'lastName')
    REGION_FIELD = (By.XPATH, '//div[contains(@class, "register-form__dropdown")]//input')
    REGIONS = (By.XPATH, '//div[contains(@class, "rt-scrollbar")]/div')
    EMAIL_PHONE_FIELD = (By.ID, 'address')
    PASSWORD_FIELD = (By.ID, 'password')
    PASSWORD_CONFIRM = (By.ID, 'password-confirm')
    SUBMIT_BUTTON = (By.CLASS_NAME, 'register-form__reg-btn')
    LICENSE_AGREEMENT = (By.XPATH, '//a[@href="https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"]')
    INPUT_ERROR = (By.CLASS_NAME, 'rt-input-container__meta--error')
    # expected text of elements
    LEFT_BLOCK_CONTENT = ('Личный кабинет', 'Персональный помощник в цифровом мире Ростелекома')
    RIGHT_BLOCK_CONTENT = ('Регистрация', 'Личные данные', 'Данные для входа')
    SUBMIT_BUTTON_NAME = 'Продолжить'
    INPUT_ERROR_MESSAGE = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'

    @property
    def left_block(self):
        return self.find_element(self.LEFT_BLOCK, 10)

    @property
    def right_block(self):
        return self.find_element(self.RIGHT_BLOCK, 10)

    @property
    def title(self):
        return self.find_element(self.TITLE, 10)

    @property
    def firstname_field(self):
        return self.find_element(self.FIRSTNAME_FIELD, 5)

    @property
    def lastname_field(self):
        return self.find_element(self.LASTNAME_FIELD)

    @property
    def region_field(self):
        return self.find_element(self.REGION_FIELD)

    @property
    def email_phone_field(self):
        return self.find_element(self.EMAIL_PHONE_FIELD, 5)

    @property
    def password_field(self):
        return self.find_element(self.PASSWORD_FIELD)

    @property
    def password_confirm_field(self):
        return self.find_element(self.PASSWORD_CONFIRM)

    @property
    def submit_button(self):
        return self.find_element(self.SUBMIT_BUTTON, 1)

    @property
    def license_agreement(self):
        return self.find_element(self.LICENSE_AGREEMENT)

    @property
    def input_errors(self):
        return self.find_elements(self.INPUT_ERROR)

    def open_registration_form(self):
        if not self.submit_button:
            ap = AuthPage(self.driver)
            ap.open_auth_form()
            self.find_element(AuthPage.REGISTRATION, 10).click()
        else:
            return

    def enter_firstname(self, firstname):
        firstname_field = self.firstname_field
        self.clear_field(firstname_field)
        firstname_field.click()
        firstname_field.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_field = self.lastname_field
        self.clear_field(lastname_field)
        lastname_field.click()
        lastname_field.send_keys(lastname)

    def pick_random_region(self):
        menu = self.find_element(self.REGION_FIELD)
        menu.click()
        regions = self.find_elements(self.REGIONS)
        rnd_index = randint(0, len(regions) - 1)
        regions[rnd_index].click()

    def enter_email_or_phone(self, text):
        field = self.email_phone_field
        self.clear_field(field)
        field.click()
        field.send_keys(text)

    def enter_password_and_confirm(self, password):
        for field in [self.password_field, self.password_confirm_field]:
            self.clear_field(field)
            field.click()
            field.send_keys(password)
