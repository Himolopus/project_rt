import pytest
from data.tests_data import testdata

from selenium.webdriver.common.keys import Keys
from time import sleep

class TestAuthFormWithoutSubmit:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser, auth_page):
        self.driver = browser
        self.auth_page = auth_page
        self.auth_page.open_auth_form()

    @pytest.mark.xfail
    def test_page_has_correct_content(self):
        for content_part in self.auth_page.LEFT_BLOCK_CONTENT:
            assert content_part in self.auth_page.left_block.text, 'Missing or wrong content in left block'

        for content_part in self.auth_page.RIGHT_BLOCK_CONTENT:
            assert content_part in self.auth_page.right_block.text, 'Missing or wrong content in right block'

        assert self.auth_page.username_field
        assert self.auth_page.password_field

    def test_default_tab_is_phone(self):
        assert self.auth_page.active_tab.text == self.auth_page.PHONE_TAB_NAME

    def test_all_form_tabs_is_functioning(self):
        self.auth_page.account_number_tab.click()
        assert self.auth_page.active_tab == self.auth_page.account_number_tab, 'Active tab is not account tab'
        assert self.auth_page.username_placeholder.text == self.auth_page.ACCOUNT_NUMBER_FIELD_PLACEHOLDER

        self.auth_page.login_tab.click()
        assert self.auth_page.active_tab == self.auth_page.login_tab, 'Active tab is not login tab'
        assert self.auth_page.username_placeholder.text == self.auth_page.LOGIN_FIELD_PLACEHOLDER

        self.auth_page.email_tab.click()
        assert self.auth_page.active_tab == self.auth_page.email_tab, 'Active tab is not email tab'
        assert self.auth_page.username_placeholder.text == self.auth_page.EMAIL_FIELD_PLACEHOLDER

        self.auth_page.phone_tab.click()
        assert self.auth_page.active_tab == self.auth_page.phone_tab, 'Active tab is not phone tab'
        assert self.auth_page.username_placeholder.text == self.auth_page.PHONE_FIELD_PLACEHOLDER

    @pytest.mark.xfail
    def test_phone_field_reacts_correctly_on_alternative_login_type_data(self):
        email_example = testdata.email_example
        self.auth_page.phone_tab.click()
        self.auth_page.enter_text_in_clean_username_field(email_example)
        assert self.auth_page.username_field.get_attribute('value') == email_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.email_tab, 'Active tab is not email tab'

        login_example = testdata.login_example
        self.auth_page.phone_tab.click()
        self.auth_page.enter_text_in_clean_username_field(login_example)
        assert self.auth_page.username_field.get_attribute('value') == login_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.login_tab, 'Active tab is not login tab'

        account_number_example = testdata.account_number_example
        self.auth_page.phone_tab.click()
        self.auth_page.enter_text_in_clean_username_field(account_number_example)
        assert self.auth_page.username_field.get_attribute('value') == account_number_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.account_number_tab, 'Active tab is not account tab'

    @pytest.mark.xfail
    def test_email_field_reacts_correctly_on_alternative_login_type_data(self):
        phone_example = testdata.phone_example
        self.auth_page.email_tab.click()
        self.auth_page.enter_text_in_clean_username_field(phone_example)
        assert self.auth_page.username_field.get_attribute('value') == phone_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.phone_tab, 'Active tab is not phone tab'

        login_example = testdata.login_example
        self.auth_page.email_tab.click()
        self.auth_page.enter_text_in_clean_username_field(login_example)
        assert self.auth_page.username_field.get_attribute('value') == login_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.login_tab, 'Active tab is not login tab'

        account_number_example = testdata.account_number_example
        self.auth_page.email_tab.click()
        self.auth_page.enter_text_in_clean_username_field(account_number_example)
        assert self.auth_page.username_field.get_attribute('value') == account_number_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.account_number_tab, 'Active tab is not account tab'

    @pytest.mark.xfail
    def test_login_field_reacts_correctly_on_alternative_login_type_data(self):
        phone_example = testdata.phone_example
        self.auth_page.login_tab.click()
        self.auth_page.enter_text_in_clean_username_field(phone_example)
        assert self.auth_page.username_field.get_attribute('value') == phone_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.phone_tab, 'Active tab is not phone tab'

        email_example = testdata.email_example
        self.auth_page.login_tab.click()
        self.auth_page.enter_text_in_clean_username_field(email_example)
        assert self.auth_page.username_field.get_attribute('value') == email_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.email_tab, 'Active tab is not email tab'

        account_number_example = testdata.account_number_example
        self.auth_page.login_tab.click()
        self.auth_page.enter_text_in_clean_username_field(account_number_example)
        assert self.auth_page.username_field.get_attribute('value') == account_number_example
        self.auth_page.password_field.click()
        assert self.auth_page.active_tab == self.auth_page.account_number_tab, 'Active tab is not account tab'

    @pytest.mark.xfail
    def test_account_number_field_reacts_correctly_on_alternative_login_type_data(self):
        phone_example = testdata.phone_example
        self.auth_page.account_number_tab.click()
        self.auth_page.enter_text_in_clean_username_field(phone_example)
        assert self.auth_page.username_field.get_attribute('value') == phone_example
        self.auth_page.password_field.click()
        phone_tab = self.auth_page.find_element(self.auth_page.PHONE_TAB)
        active_tab = self.auth_page.find_element(self.auth_page.ACTIVE_TAB)
        assert active_tab == phone_tab, 'Active tab is not phone tab'

        email_example = testdata.email_example
        self.auth_page.account_number_tab.click()
        self.auth_page.enter_text_in_clean_username_field(email_example)
        assert self.auth_page.username_field.get_attribute('value') == email_example
        self.auth_page.password_field.click()
        email_tab = self.auth_page.find_element(self.auth_page.EMAIL_TAB)
        active_tab = self.auth_page.find_element(self.auth_page.ACTIVE_TAB)
        assert active_tab == email_tab, 'Active tab is not email tab'

        login_example = testdata.login_example
        self.auth_page.account_number_tab.click()
        self.auth_page.enter_text_in_clean_username_field(login_example)
        assert self.auth_page.username_field.get_attribute('value') == login_example
        self.auth_page.password_field.click()
        login_tab = self.auth_page.find_element(self.auth_page.LOGIN_TAB)
        active_tab = self.auth_page.find_element(self.auth_page.ACTIVE_TAB)
        assert active_tab == login_tab, 'Active tab is not login tab'

    def test_submit_attempt_form_with_empty_fields(self, tabs_data):
        tab_locator, username, error_message = tabs_data

        self.auth_page.find_element(tab_locator).click()
        self.auth_page.clear_username_field()
        self.auth_page.clear_password_field()
        self.auth_page.submit_button.click()
        assert self.auth_page.username_field
        assert self.auth_page.input_error_message.text == error_message

        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.auth_page.submit_button.click()
        assert self.auth_page.username_field
        assert self.auth_page.input_error_message.text == error_message

        self.auth_page.clear_password_field()
        self.auth_page.enter_text_in_clean_username_field(username)
        self.auth_page.submit_button.click()
        assert self.auth_page.username_field

    def test_form_fields_cleared_after_page_refresh(self):
        self.auth_page.enter_text_in_clean_username_field(testdata.login_example)
        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.driver.refresh()
        assert self.auth_page.username_field.get_attribute('value') == ''
        assert self.auth_page.password_field.get_attribute('value') == ''


class TestAuthFormWithSubmit:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser, auth_page, home_page):
        self.driver = browser
        self.auth_page = auth_page
        self.home_page = home_page
        self.auth_page.open_auth_form()
        self.auth_page.check_captcha()

    @pytest.mark.skip
    def test_auth_by_phone_number_with_valid_data(self):
        self.auth_page.phone_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_PHONE_NUMBER)
        self.auth_page.enter_text_in_clean_password_field(testdata.REGISTERED_PASSWORD)
        self.auth_page.click_submit()
        assert self.home_page.logout_button
        assert self.home_page.info_card

    @pytest.mark.skip
    def test_auth_by_email_with_valid_data(self):
        self.auth_page.email_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_EMAIL)
        self.auth_page.enter_text_in_clean_password_field(testdata.REGISTERED_PASSWORD)
        self.auth_page.click_submit()
        assert self.home_page.logout_button
        assert self.home_page.info_card

    @pytest.mark.skip
    def test_auth_by_login_with_valid_data(self):
        self.auth_page.login_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_LOGIN)
        self.auth_page.enter_text_in_clean_password_field(testdata.REGISTERED_PASSWORD)
        self.auth_page.click_submit()
        assert self.home_page.logout_button
        assert self.home_page.info_card

    @pytest.mark.skip
    def test_auth_by_account_number_with_valid_data(self):
        self.auth_page.account_number_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_ACCOUNT_NUMBER)
        self.auth_page.enter_text_in_clean_password_field(testdata.REGISTERED_PASSWORD)
        self.auth_page.click_submit()
        assert self.home_page.logout_button
        assert self.home_page.info_card
        
    @pytest.mark.skip
    def test_auth_by_phone_number_with_invalid_password(self):
        self.auth_page.phone_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_PHONE_NUMBER)
        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.auth_page.click_submit()
        assert self.auth_page.form_error_message
        assert self.auth_page.form_error_message.text == self.auth_page.WRONG_LOGIN_OR_PASSWORD_ERROR

    @pytest.mark.skip
    def test_auth_by_email_number_with_invalid_password(self):
        self.auth_page.email_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_EMAIL)
        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.auth_page.click_submit()
        assert self.auth_page.form_error_message
        assert self.auth_page.form_error_message.text == self.auth_page.WRONG_LOGIN_OR_PASSWORD_ERROR

    @pytest.mark.skip
    def test_auth_by_login_with_invalid_password(self):
        self.auth_page.login_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_LOGIN)
        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.auth_page.click_submit()
        assert self.auth_page.form_error_message
        assert self.auth_page.form_error_message.text == self.auth_page.WRONG_LOGIN_OR_PASSWORD_ERROR

    @pytest.mark.skip
    def test_auth_by_account_number_with_invalid_password(self):
        self.auth_page.account_number_tab.click()
        self.auth_page.enter_text_in_clean_username_field(testdata.REGISTERED_ACCOUNT_NUMBER)
        self.auth_page.enter_text_in_clean_password_field(testdata.password_example)
        self.auth_page.click_submit()
        assert self.auth_page.form_error_message
        assert self.auth_page.form_error_message.text == self.auth_page.WRONG_LOGIN_OR_PASSWORD_ERROR

    @pytest.mark.skip
    def test_sending_long_string_and_incorrect_symbols_in_password(self, wrong_format_auth_password):
        self.auth_page.enter_text_in_clean_username_field(testdata.login_example)
        self.auth_page.enter_text_in_clean_password_field(wrong_format_auth_password)
        self.auth_page.submit_button.click()
        assert self.auth_page.form_error_message
        assert self.auth_page.form_error_message.text == self.auth_page.WRONG_LOGIN_OR_PASSWORD_ERROR


class TestRegistrationForm:

    @pytest.fixture(autouse=True)
    def setup_method(self, browser, reg_page, confirm_page):
        self.driver = browser
        self.reg_page = reg_page
        self.confirm_page = confirm_page
        self.reg_page.open_registration_form()

    @pytest.mark.xfail
    def test_page_has_correct_content(self):
        for content_part in self.reg_page.LEFT_BLOCK_CONTENT:
            assert content_part in self.reg_page.left_block.text, 'Missing or wrong content in left block'

        for content_part in self.reg_page.RIGHT_BLOCK_CONTENT:
            assert content_part in self.reg_page.right_block.text, 'Missing or wrong content in right block'

        assert self.reg_page.firstname_field
        assert self.reg_page.left_block
        assert self.reg_page.region_field
        assert self.reg_page.email_phone_field
        assert self.reg_page.password_field
        assert self.reg_page.password_confirm_field
        assert self.reg_page.submit_button.text == self.reg_page.SUBMIT_BUTTON_NAME
        assert self.reg_page.license_agreement

    def test_reg_attempt_by_phone_number_with_invalid_confirm_code(self):
        self.reg_page.enter_firstname(testdata.firstname_example)
        self.reg_page.enter_lastname(testdata.lastname_example)
        self.reg_page.pick_random_region()
        self.reg_page.enter_email_or_phone(testdata.phone_example)
        self.reg_page.enter_password_and_confirm(testdata.password_example)
        self.reg_page.submit_button.click()
        assert self.confirm_page.title
        assert self.confirm_page.title.text == self.confirm_page.PHONE_CONFIRM_TITLE
        self.confirm_page.enter_code(testdata.code_example)
        assert self.confirm_page.error_message
        assert self.confirm_page.error_message.text

    def test_reg_attempt_by_email_with_invalid_confirm_code(self):
        self.reg_page.enter_firstname(testdata.firstname_example)
        self.reg_page.enter_lastname(testdata.lastname_example)
        self.reg_page.pick_random_region()
        self.reg_page.enter_email_or_phone(testdata.email_example)
        self.reg_page.enter_password_and_confirm(testdata.password_example)
        self.reg_page.submit_button.click()
        assert self.confirm_page.title
        assert self.confirm_page.title.text == self.confirm_page.EMAIL_CONFIRM_TITLE
        self.confirm_page.enter_code(testdata.code_example)
        assert self.confirm_page.error_message
        assert self.confirm_page.error_message.text

    def test_boundary_values_of_name_in_reg_form(self, name_boundary_value):
        value, is_valid = name_boundary_value
        if self.reg_page.email_phone_field.get_attribute('value') == '':
            self.reg_page.enter_email_or_phone(testdata.email_example)
        if self.reg_page.password_confirm_field.get_attribute('value') == '':
            self.reg_page.enter_password_and_confirm(testdata.password_example)
        self.reg_page.pick_random_region()
        self.reg_page.enter_firstname(value)
        self.reg_page.enter_lastname(value)
        self.reg_page.title.click()
        self.reg_page.submit_button.click()
        if is_valid:
            assert self.confirm_page.code_field
        else:
            assert len(self.reg_page.input_errors) == 2
            assert self.reg_page.input_errors[0].text == self.reg_page.INPUT_ERROR_MESSAGE
            assert self.reg_page.input_errors[1].text == self.reg_page.INPUT_ERROR_MESSAGE

    def test_invalid_values_of_name_in_reg_form(self, name_invalid_value):
        value = name_invalid_value
        if self.reg_page.email_phone_field.get_attribute('value') == '':
            self.reg_page.enter_email_or_phone(testdata.email_example)
        if self.reg_page.password_confirm_field.get_attribute('value') == '':
            self.reg_page.enter_password_and_confirm(testdata.password_example)
        self.reg_page.pick_random_region()
        self.reg_page.enter_firstname(value)
        self.reg_page.enter_lastname(value)
        self.reg_page.title.click()
        self.reg_page.submit_button.click()
        assert len(self.reg_page.input_errors) == 2
        assert self.reg_page.input_errors[0].text == self.reg_page.INPUT_ERROR_MESSAGE
        assert self.reg_page.input_errors[1].text == self.reg_page.INPUT_ERROR_MESSAGE
