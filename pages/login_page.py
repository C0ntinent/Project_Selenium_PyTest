from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


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
