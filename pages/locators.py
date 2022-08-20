from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PASSWORD = (By.NAME, 'login-password')
    REGISTER_EMAIL = (By.NAME, 'registration-email')
    REGISTER_PASSWORD1 = (By.NAME, 'registration-password1')
    REGISTER_PASSWORD2 = (By.NAME, 'registration-password2')


class ProductPageLocators:
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '.alertinner>p>strong')
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, '.alertinner>strong')
