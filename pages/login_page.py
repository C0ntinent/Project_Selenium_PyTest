from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Invalid URL"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_EMAIL) and \
               self.is_element_present(
                   *LoginPageLocators.LOGIN_PASSWORD), "Login form is not " \
                                                       "presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_EMAIL) and \
               self.is_element_present(
                   *LoginPageLocators.REGISTER_PASSWORD1) and \
               self.is_element_present(
                   *LoginPageLocators.REGISTER_PASSWORD2), "Register form is " \
                                                           "not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTER_EMAIL).send_keys(f"{email}")
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD1).send_keys(f"{password}")
        self.browser.find_element(
            *LoginPageLocators.REGISTER_PASSWORD2).send_keys(f"{password}")
        self.browser.find_element(*LoginPageLocators.BUTTON_OF_REGISTER).click()

