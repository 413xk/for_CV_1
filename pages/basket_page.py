from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    pass

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), 'Some items in the basket'

    def should_be_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text == \
               'Your basket is empty. Continue shopping'
