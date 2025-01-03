from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_no_product(self):
        assert self.is_not_element_present(*BasketPageLocators.ADDED_PRODUCT), \
            "Added product is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET),\
            "Basket is not empty"