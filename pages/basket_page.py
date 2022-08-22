from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.TOTAL_PRICE), \
            "Busket is not empty!"

    def should_be_empty_basket_message(self):
        empty_basket = self.browser.find_element(
            *BasketPageLocators.BASKET_IS_EMPTY).text
        assert not self.is_not_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY) and empty_basket, \
            "Basket is not empty, but should be!"
