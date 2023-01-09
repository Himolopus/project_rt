import pytest
from selenium import webdriver
from pages.base_page import BasePage
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.phone_email_confirm_page import PhoneEmailConfirmPage
from data.tests_data import testdata


@pytest.fixture(scope='session', params=['chrome', ])
def browser(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'msedge':
        driver = webdriver.Edge()
    else:
        raise TypeError('No params')
    driver.maximize_window()
    driver.get(BasePage.URL)

    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def auth_page(browser):
    page = AuthPage(browser)
    return page


@pytest.fixture(scope='session')
def home_page(browser):
    page = HomePage(browser)
    return page


@pytest.fixture(scope='session')
def reg_page(browser):
    page = RegistrationPage(browser)
    return page


@pytest.fixture(scope='session')
def confirm_page(browser):
    page = PhoneEmailConfirmPage(browser)
    return page


@pytest.fixture(scope='function', params=['account_number', 'login', 'email', 'phone'])
def tabs_data(request):
    if request.function.__name__ == 'test_submit_attempt_form_with_empty_fields':
        tab_locator, username, error_message = (None, None, None)
        if request.param == 'account_number':
            tab_locator = AuthPage.ACCOUNT_NUMBER_TAB
            username = testdata.REGISTERED_ACCOUNT_NUMBER
            error_message = AuthPage.EMPTY_ACCOUNT_NUMBER_ERROR
        elif request.param == 'login':
            tab_locator = AuthPage.LOGIN_TAB
            username = testdata.REGISTERED_LOGIN
            error_message = AuthPage.EMPTY_LOGIN_ERROR
        elif request.param == 'email':
            tab_locator = AuthPage.EMAIL_TAB
            username = testdata.REGISTERED_EMAIL
            error_message = AuthPage.EMPTY_EMAIL_ERROR
        elif request.param == 'phone':
            tab_locator = AuthPage.PHONE_TAB
            username = testdata.REGISTERED_PHONE_NUMBER
            error_message = AuthPage.EMPTY_PHONE_NUMBER_ERROR
        return tab_locator, username, error_message


@pytest.fixture(scope='function',
                params=[testdata.string_with_spaces_and_tabs, testdata.string_with_cyrillic, testdata.string_255,
                        testdata.string_1000],
                ids=['spaces', 'cyrillic', '255', '1000'])
def wrong_format_auth_password(request):
    string = request.param
    return string


@pytest.fixture(scope='function',
                params=[testdata.get_cyrillic_string(1), testdata.get_cyrillic_string(2),
                        testdata.get_cyrillic_string(30), testdata.get_cyrillic_string(31)],
                ids=['cyrillic 1 char', 'cyrillic 2 chars', 'cyrillic 30 chars',
                     'cyrillic 31 chars'])
def name_boundary_value(request):
    is_valid = True if request.param_index in [1, 2] else False
    return request.param, is_valid


@pytest.fixture(scope='function',
                params=['', testdata.cyrillic_string_with_digits, testdata.cyrillic_string_with_special,
                        testdata.cyrillic_string_with_spaces, testdata.cyrillic_and_latin_string],
                ids=['empty string', 'cyrillic plus digits', 'cyrillic plus special chars',
                     'cyrillic with spaces', 'cyrillic and latin'])
def name_invalid_value(request):
    return request.param
