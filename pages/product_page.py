import math

from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import ItemPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_add_to_basket_button()

    def should_be_correct_page_data(self):
        self.should_be_correct_price_in_basket()
        self.should_be_correct_name_item_in_basket()

    def should_be_product_url(self):
        assert '/catalogue/' in self.browser.current_url, "You're not on item's page"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ItemPageLocators.ADD_TO_BASKET_BUTTON), \
            "No button 'add to basket' on this page"

    def should_be_correct_price_in_basket(self):
        self.browser.implicitly_wait(10)
        assert self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text == \
               self.browser.find_element(*ItemPageLocators.ADDED_ITEM_PRICE).text, \
            'Price in the basket is different or not found'

    def should_be_correct_name_item_in_basket(self):
        self.browser.implicitly_wait(10)
        assert self.browser.find_element(*ItemPageLocators.ITEM_NAME).text == \
               self.browser.find_element(*ItemPageLocators.ADDED_ITEM_NAME).text, \
            "Item's name in the basket is different or not found"

    def should_be_correct_answer(self):
        self.solve_quiz_and_get_code()

    def should_be_login_page(self):
        assert '/login/' in self.browser.current_url, "You're not on item's page"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #  1.11 add checking for success messages
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE), \
            'Success message do not disappear'
