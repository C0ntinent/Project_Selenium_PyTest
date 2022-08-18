import time
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage


def test_guest_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_in_basket()