import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class AuthPage(BasePage):
    # locators
    LEFT_BLOCK = (By.ID, 'page-left')
    RIGHT_BLOCK = (By.ID, 'page-right')
    USERNAME_FIELD = (By.ID, 'username')
    USERNAME_PLACEHOLDER = (By.XPATH, '//div[contains(@class, "tabs-input-container__login")]'
                                      '//span[contains(@class, "rt-input__placeholder")]')
    PASSWORD_FIElD = (By.ID, 'password')
    SUBMIT_BUTTON = (By.ID, 'kc-login')
    ACTIVE_TAB = (By.CLASS_NAME, 'rt-tab--active')
    PHONE_TAB = (By.ID, 't-btn-tab-phone')
    EMAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOGIN_TAB = (By.ID, 't-btn-tab-login')
    ACCOUNT_NUMBER_TAB = (By.ID, 't-btn-tab-ls')
    FORM_ERROR_MESSAGE = (By.ID, 'form-error-message')
    INPUT_ERROR_MESSAGE = (By.CLASS_NAME, 'rt-input-container__meta--error')
    CAPTCHA = (By.CLASS_NAME, 'login-form__captcha')
    REGISTRATION = (By.ID, 'kc-register')
    # expected text of elements
    LEFT_BLOCK_CONTENT = ('Телефон', 'Почта', 'Логин', 'Лицевой сч')
    RIGHT_BLOCK_CONTENT = ('Ростелеком ID', )
    PHONE_TAB_NAME = 'Телефон'
    EMAIL_TAB_NAME = 'Почта'
    LOGIN_TAB_NAME = 'Логин'
    ACCOUNT_NUMBER_TAB_NAME = ('Лицевой счёт', 'Лицевой счет')
    PHONE_FIELD_PLACEHOLDER = 'Мобильный телефон'
    EMAIL_FIELD_PLACEHOLDER = 'Электронная почта'
    LOGIN_FIELD_PLACEHOLDER = 'Логин'
    ACCOUNT_NUMBER_FIELD_PLACEHOLDER = 'Лицевой счёт'
    WRONG_LOGIN_OR_PASSWORD_ERROR = 'Неверный логин или пароль'
    EMPTY_PHONE_NUMBER_ERROR = 'Введите номер телефона'
    EMPTY_EMAIL_ERROR = 'Введите адрес, указанный при регистрации'
    EMPTY_LOGIN_ERROR = 'Введите логин, указанный при регистрации'
    EMPTY_ACCOUNT_NUMBER_ERROR = 'Введите номер вашего лицевого счета'

    @property
    def left_block(self):
        return self.find_element(self.LEFT_BLOCK, 10)

    @property
    def right_block(self):
        return self.find_element(self.RIGHT_BLOCK, 10)

    @property
    def phone_tab(self):
        return self.find_element(self.PHONE_TAB)

    @property
    def email_tab(self):
        return self.find_element(self.EMAIL_TAB)

    @property
    def login_tab(self):
        return self.find_element(self.LOGIN_TAB)

    @property
    def account_number_tab(self):
        return self.find_element(self.ACCOUNT_NUMBER_TAB)

    @property
    def active_tab(self):
        return self.find_element(self.ACTIVE_TAB)

    @property
    def username_field(self):
        return self.find_element(self.USERNAME_FIELD, 3)

    @property
    def username_placeholder(self):
        return self.find_element(self.USERNAME_PLACEHOLDER)

    @property
    def password_field(self):
        return self.find_element(self.PASSWORD_FIElD, 3)

    @property
    def submit_button(self):
        return self.find_element(self.SUBMIT_BUTTON)

    @property
    def form_error_message(self):
        return self.find_element(self.FORM_ERROR_MESSAGE, 1)

    @property
    def input_error_message(self):
        return self.find_element(self.INPUT_ERROR_MESSAGE, 1)

    def enter_text_in_clean_username_field(self, username):
        username_field = self.username_field
        self.clear_field(username_field)
        username_field.click()
        username_field.send_keys(username)

    def enter_text_in_clean_password_field(self, password):
        password_field = self.password_field
        self.clear_field(password_field)
        password_field.click()
        password_field.send_keys(password)

    def clear_username_field(self):
        self.clear_field(self.username_field)

    def clear_password_field(self):
        self.clear_field(self.password_field)

    def click_submit(self):
        self.submit_button.click()

    def open_auth_form(self):
        if self.submit_button:
            return
        elif self.driver.current_url.startswith('https://b2c.passport.rt.ru/account'):
            logout_button = self.find_element(HomePage.LOGOUT_BUTTON)
            logout_button.click()
        else:
            self.open_page()

    def is_there_a_captcha(self):
        return bool(self.find_element(self.CAPTCHA))

    def check_captcha(self):
        captcha = self.find_element(self.CAPTCHA)
        if captcha:
            assert False, 'CAPTCHA is present'