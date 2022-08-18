from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()

    def should_be_product_url(self):
        assert "?promo=newYear" in self.browser.current_url, "Invalid URL"

    def should_be_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_BUTTON), "Basket button is " \
                                                 "not presented"

    def product_in_basket(self):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_BASKET).text and self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(
                   *ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text, 'PRODUCT IS NOT IN BASKET'
