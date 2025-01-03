from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = ()
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    USER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    USER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_ACCEPT = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-lg")

    REGISTER_COMPLITED = (By.CSS_SELECTOR, "div.alert-success")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE =(By.CSS_SELECTOR, ".product_main p.price_color")

    BASKET_NAME = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn-default")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ADDED_PRODUCT = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
